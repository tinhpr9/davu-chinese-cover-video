#!/usr/bin/env python3
"""
Accurately extract all lyric events and exact timestamps from the source video.
Detects subtitle changes using MSE / pixel diff, then runs tesseract OCR.
"""
import subprocess
import os
import json
import numpy as np
from PIL import Image

def extract_timeline(video_path="assets/loHupy4MWmc_360p.mp4", tmp_dir="output/ocr_frames"):
    os.makedirs(tmp_dir, exist_ok=True)
    
    # 1. Sample frames at 2 fps (every 0.5s)
    print("Extracting frames at 2 fps...")
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-vf", "fps=2,crop=580:130:30:225",
        f"{tmp_dir}/frame_%04d.png"
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    
    files = sorted([f for f in os.listdir(tmp_dir) if f.startswith("frame_") and f.endswith(".png")])
    print(f"Total sampled frames: {len(files)}")
    
    # 2. Group into contiguous segments based on image similarity
    segments = []
    current_seg = {"start_idx": 0, "file": files[0], "frames": [files[0]]}
    
    prev_arr = np.array(Image.open(os.path.join(tmp_dir, files[0])).convert("L"))
    
    for i in range(1, len(files)):
        fname = files[i]
        curr_arr = np.array(Image.open(os.path.join(tmp_dir, fname)).convert("L"))
        # Calculate mean absolute difference
        diff = np.mean(np.abs(curr_arr.astype(float) - prev_arr.astype(float)))
        
        # If diff > threshold, lyric changed
        if diff > 15.0:
            current_seg["end_idx"] = i - 1
            segments.append(current_seg)
            current_seg = {"start_idx": i, "file": fname, "frames": [fname]}
        else:
            current_seg["frames"].append(fname)
            
        prev_arr = curr_arr
        
    current_seg["end_idx"] = len(files) - 1
    segments.append(current_seg)
    
    print(f"Detected {len(segments)} candidate segments.")
    
    # 3. Run OCR on middle frame of each candidate segment
    lyric_events = []
    for seg in segments:
        duration_frames = seg["end_idx"] - seg["start_idx"] + 1
        start_time = seg["start_idx"] * 0.5
        end_time = (seg["end_idx"] + 1) * 0.5
        
        # Subtitles lasting < 1.0s might be flicker/transition
        if duration_frames < 2:
            continue
            
        mid_file = seg["frames"][len(seg["frames"]) // 2]
        img_path = os.path.join(tmp_dir, mid_file)
        
        # Check if frame is mostly blank (black)
        img_arr = np.array(Image.open(img_path).convert("L"))
        if np.max(img_arr) < 80:  # dark/blank
            continue
            
        # Run tesseract
        res = subprocess.run(
            ["tesseract", img_path, "stdout", "-l", "chi_sim+vie", "--psm", "6"],
            capture_output=True, text=True
        )
        lines = [l.strip() for l in res.stdout.split("\n") if l.strip()]
        
        if len(lines) >= 2:
            lyric_events.append({
                "start": start_time,
                "end": end_time,
                "lines": lines,
                "raw_text": " | ".join(lines)
            })
            print(f"[{start_time:06.2f} -> {end_time:06.2f}]: {lines}")
            
    out_json = "output/extracted_lyrics.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(lyric_events, f, ensure_ascii=False, indent=2)
        
    print(f"Saved {len(lyric_events)} lyrics to {out_json}")
    return lyric_events

if __name__ == "__main__":
    extract_timeline()
