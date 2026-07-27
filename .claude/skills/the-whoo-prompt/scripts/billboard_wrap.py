#!/usr/bin/env python3
"""Corner-pin a clip onto the corner-wrapping billboard and encode.

Corners come from fitting straight lines to the panel's rim in the plate and
intersecting them, so both planes are the true projection of a rectangle — a
hand-placed quad reads as a flat sticker instead of a screen.

The LED pixel lattice is drawn in the clip's own space and pushed through the
same homography, so it converges with the surface the way real pitch does.
"""

import argparse
import subprocess

import cv2
import imageio_ffmpeg
import numpy as np

# solved off the plate: rim lines fitted, then intersected
TL = (1057.8, 611.4)        # far top-left of the main face
CORNER_T = (1827.5, 198.4)  # top of the vertical fold
CORNER_B = (1872.1, 854.3)  # bottom of the fold
BL = (984.4, 959.8)
TR = (2127.9, 317.1)        # far top-right of the side face
BR = (2190.4, 890.2)

MAIN_FACE = np.float32([TL, CORNER_T, CORNER_B, BL])    # big, faces the camera
SIDE_FACE = np.float32([CORNER_T, TR, BR, CORNER_B])    # narrow, angled away


def build_grid(vh, vw, pitch, strength):
    g = np.ones((vh, vw), np.float32)
    g[::pitch, :] *= 1 - strength
    g[:, ::pitch] *= 1 - strength
    return cv2.merge([g] * 3)


def led_look(frame, gain, sat, lift):
    f = np.clip(frame.astype(np.float32) * gain + lift, 0, 255).astype(np.uint8)
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[..., 1] = np.clip(hsv[..., 1] * sat, 0, 255)
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR).astype(np.float32)


def main(a):
    plate = cv2.imread(a.bg)
    H, W = plate.shape[:2]

    cap = cv2.VideoCapture(a.video)
    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    vw = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    vh = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    n_out = int(round(a.duration * fps)) if a.duration else int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    src = np.float32([[0, 0], [vw, 0], [vw, vh], [0, vh]])
    M_main = cv2.getPerspectiveTransform(src, MAIN_FACE)
    M_side = cv2.getPerspectiveTransform(src, SIDE_FACE)

    def mask_for(quad, feather=1.2):
        m = np.zeros((H, W), np.float32)
        cv2.fillConvexPoly(m, np.int32(quad), 1.0)
        return cv2.merge([cv2.GaussianBlur(m, (0, 0), feather)] * 3)

    m_main, m_side = mask_for(MAIN_FACE), mask_for(SIDE_FACE)

    # the quads are the ideal rectangle; the plate's own white area is where the
    # panel is actually visible. Clipping to it keeps content off the roofline
    # and storefront that cut into the bottom-left corner.
    if a.clip_mask:
        lit_area = cv2.imread(a.clip_mask, 0)
        lit_area = cv2.erode(lit_area, np.ones((3, 3), np.uint8))
        lit_area = cv2.merge([cv2.GaussianBlur(lit_area, (0, 0), 1.2).astype(np.float32) / 255.0] * 3)
        m_main *= lit_area
        m_side *= lit_area

    panel = np.clip(m_main + m_side, 0, 1)

    # the lattice lives in clip space, so warping it makes the pitch converge
    grid_src = build_grid(vh, vw, a.grid_pitch, a.grid_strength)
    grid_main = cv2.warpPerspective(grid_src, M_main, (W, H), borderValue=(1, 1, 1))
    grid_side = cv2.warpPerspective(grid_src, M_side, (W, H), borderValue=(1, 1, 1))

    spill = np.clip(cv2.GaussianBlur(panel, (0, 0), max(W, H) * 0.045) - panel, 0, 1) * a.glow

    ff = subprocess.Popen(
        [imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-f", "rawvideo", "-pix_fmt", "bgr24",
         "-s", f"{W}x{H}", "-r", f"{fps}", "-i", "-", "-an",
         "-vf", f"scale={a.scale}:-2", "-c:v", "libx264", "-preset", "medium",
         "-crf", "17", "-pix_fmt", "yuv420p", a.out],
        stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for i in range(n_out):
        ok, frame = cap.read()
        if not ok:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ok, frame = cap.read()
            if not ok:
                break
        lit = led_look(frame, a.gain, a.saturation, a.lift)

        out = plate.astype(np.float32)
        w_main = cv2.warpPerspective(lit, M_main, (W, H), flags=cv2.INTER_CUBIC) * grid_main
        out = out * (1 - m_main) + w_main * m_main

        if a.side == "dark":
            w_side = np.full_like(out, a.side_level) * grid_side
        else:
            w_side = cv2.warpPerspective(lit, M_side, (W, H), flags=cv2.INTER_CUBIC) * grid_side
        out = out * (1 - m_side) + w_side * m_side

        tint = cv2.mean(out, mask=(panel[..., 0] * 255).astype(np.uint8))[:3]
        out = np.clip(out + spill * np.float32(tint), 0, 255)

        if a.zoom > 0:
            z = 1.0 + a.zoom * (i / max(n_out - 1, 1))
            Mz = cv2.getRotationMatrix2D((W / 2, H * 0.45), 0, z)
            out = cv2.warpAffine(out, Mz, (W, H), flags=cv2.INTER_CUBIC)

        ff.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())

    cap.release()
    ff.stdin.close()
    ff.wait()
    print("wrote", a.out, f"({n_out} frames @ {fps:.2f}fps)")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--bg", required=True)
    p.add_argument("--video", required=True)
    p.add_argument("--out", default="final.mp4")
    p.add_argument("--duration", type=float, default=0)
    p.add_argument("--side", choices=["dark", "play"], default="dark")
    p.add_argument("--side-level", type=float, default=12.0)
    p.add_argument("--gain", type=float, default=1.25)
    p.add_argument("--lift", type=float, default=6.0)
    p.add_argument("--saturation", type=float, default=1.12)
    p.add_argument("--glow", type=float, default=0.28)
    p.add_argument("--zoom", type=float, default=0.035)
    p.add_argument("--grid-pitch", type=int, default=4)
    p.add_argument("--grid-strength", type=float, default=0.10)
    p.add_argument("--clip-mask", default=None)
    p.add_argument("--scale", type=int, default=1920)
    main(p.parse_args())
