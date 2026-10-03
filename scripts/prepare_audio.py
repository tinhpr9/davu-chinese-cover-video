#!/usr/bin/env python3
"""
Slice the viral chorus section (32.0s -> 88.0s) from Dạ Vũ Chinese cover.
Applies smooth fade-in (0.5s) and fade-out (1.5s) with high bitrate (192kbps).
"""
import subprocess
import os
import sys

def prepare_audio(input_path="assets/davu_chinese_original.mp3",
                  output_path="output/davu_chorus_56s.mp3",
                  start_time=32.0,
                  duration=56.0):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input audio file not found: {input_path}")
        
    fade_out_start = duration - 1.5
    afade_filter = f"afade=t=in:ss=0:d=0.5,afade=t=out:st={fade_out_start:.1f}:d=1.5"
    
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(start_time),
        "-t", str(duration),
        "-i", input_path,
        "-af", afade_filter,
        "-c:a", "libmp3lame",
        "-b:a", "192k",
        "-ar", "44100",
        output_path
    ]
    
    print(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error cutting audio: {result.stderr}", file=sys.stderr)
        raise RuntimeError("Failed to process audio")
        
    print(f"Successfully generated: {output_path}")
    return output_path

if __name__ == "__main__":
    prepare_audio()
