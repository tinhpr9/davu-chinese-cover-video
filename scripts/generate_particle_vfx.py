#!/usr/bin/env python3
"""
Procedural Cinematic Particle Engine for Dạ Vũ Cổ Phong Video.
Generates a seamless 10-second (300 frames @ 30fps) 1080x1920 video containing:
1. Drifting pink & white cherry/plum blossom petals with 3D tumble physics
2. Delicate falling snow crystals
"""
import os
import math
import numpy as np
from PIL import Image, ImageDraw
import subprocess
import time

def generate_particle_video(output_path="assets/particles_loop.mp4", duration=10, fps=30):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    width, height = 1080, 1920
    total_frames = duration * fps
    
    print(f"Generating {total_frames} frames of natural blossom & snow particles ({width}x{height} @ {fps}fps)...")
    start_time = time.time()
    
    np.random.seed(42)
    
    # 1. Initialize Petals (80 petals: varied sizes and drift)
    num_petals = 80
    petals = []
    for _ in range(num_petals):
        petals.append({
            "x0": np.random.uniform(-50, width + 50),
            "y0": np.random.uniform(-100, height + 100),
            "speed_y": np.random.uniform(70, 160), # pixels per second
            "drift_amp": np.random.uniform(30, 80),
            "drift_freq": np.random.uniform(0.3, 0.8),
            "rot_speed": np.random.uniform(0.8, 2.5),
            "size": np.random.uniform(10, 22),
            "color": (
                np.random.randint(240, 255), # R: soft pink/rose
                np.random.randint(185, 225), # G: blossom
                np.random.randint(200, 235)  # B
            ),
            "alpha": np.random.randint(150, 230)
        })

    # 2. Initialize Snow crystals (150 snow dots)
    num_snow = 150
    snow = []
    for _ in range(num_snow):
        snow.append({
            "x0": np.random.uniform(0, width),
            "y0": np.random.uniform(0, height),
            "speed_y": np.random.uniform(100, 240),
            "drift_amp": np.random.uniform(15, 45),
            "drift_freq": np.random.uniform(0.6, 1.6),
            "radius": np.random.uniform(1.5, 4.0),
            "alpha": np.random.randint(140, 240)
        })

    # FFmpeg pipe process
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{width}x{height}",
        "-pix_fmt", "rgb24",
        "-r", str(fps),
        "-i", "-",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        output_path
    ]
    
    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
    
    for f in range(total_frames):
        t = f / fps
        
        # Black background
        frame_img = Image.new("RGBA", (width, height), (0, 0, 0, 255))
        draw = ImageDraw.Draw(frame_img)

        # Render Snow
        for s in snow:
            y = (s["y0"] + s["speed_y"] * t) % height
            x = (s["x0"] + s["drift_amp"] * math.sin(2 * math.pi * s["drift_freq"] * t)) % width
            r = s["radius"]
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(245, 248, 255, s["alpha"]))

        # Render Petals (elliptical rotating petals with soft gradient feel)
        for p in petals:
            y = (p["y0"] + p["speed_y"] * t) % height
            x = (p["x0"] + p["drift_amp"] * math.sin(2 * math.pi * p["drift_freq"] * t)) % width
            angle = p["rot_speed"] * t * 2 * math.pi
            sz = p["size"]
            r_c, g_c, b_c = p["color"]
            scale_y = abs(math.cos(angle))
            pw = sz
            ph = max(3, sz * 0.55 * scale_y)
            draw.ellipse([x - pw/2, y - ph/2, x + pw/2, y + ph/2], fill=(r_c, g_c, b_c, p["alpha"]))
            
        rgb_bytes = frame_img.convert("RGB").tobytes()
        proc.stdin.write(rgb_bytes)

    proc.stdin.close()
    proc.wait()
    
    elapsed = time.time() - start_time
    print(f"Blossom & Snow particles generated in {elapsed:.1f}s -> {output_path}")
    return output_path

if __name__ == "__main__":
    generate_particle_video()
