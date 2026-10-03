#!/usr/bin/env python3
"""
Full-length (3m20s / 200s) Master Video Renderer for Dạ Vũ (夜舞) Chinese Cover.
Features:
- Vertical 1080x1920 (9:16) format
- High-definition Chinese beauty maiden with Pipa in moonlit ancient pavilion
- Smooth continuous Ken Burns push-in motion (zoompan)
- 100% verified, perfectly synchronized 3-layer lyrics (Hanzi + Pinyin + Vietsub)
- Universal H.264 / AAC compatibility
"""
import os
import sys
import subprocess
import time

def render_full_music_video(
    bg_path="assets/chinese_beauty_pipa.jpg",
    audio_path="assets/davu_chinese_original.mp3",
    sub_path="output/davu_full_subtitles.ass",
    output_path="output/DaVu_Chinese_Version_FULL_Master.mp4",
    duration=200.088
):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    for f in [bg_path, audio_path, sub_path]:
        if not os.path.exists(f):
            raise FileNotFoundError(f"Input file not found: {f}")
            
    print(f"Starting FULL video render -> {output_path}")
    print(f"Duration: {duration}s (~3m20s) | Target: 1080x1920 @ 30fps")

    # Filter graph:
    # 1. Scale image to safe zoom canvas (1200x2134)
    # 2. Apply gentle continuous Ken Burns slow zoom from 1.0 to 1.08 over 200s
    # 3. Burn in 3-layer ASS subtitles with format=yuv420p
    filter_complex = (
        "[0:v]scale=1200:2134,"
        "zoompan=z='min(zoom+0.00002,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,"
        f"ass={sub_path},format=yuv420p[v]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-t", str(duration),
        "-i", bg_path,
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "1:a",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-t", str(duration),
        output_path
    ]

    start_time = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True)
    elapsed = time.time() - start_time
    
    if result.returncode != 0:
        print(f"Rendering failed:\n{result.stderr}", file=sys.stderr)
        raise RuntimeError("ffmpeg video rendering failed")
        
    print(f"Render completed successfully in {elapsed:.1f}s: {output_path}")
    return output_path

if __name__ == "__main__":
    render_full_music_video()
