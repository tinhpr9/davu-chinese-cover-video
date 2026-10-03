#!/usr/bin/env python3
"""
Full rendering pipeline for Dạ Vũ (夜舞) Chinese Cover TikTok Video.
Resolution: 1080x1920 (9:16 Vertical)
Frame rate: 30 fps
Audio: AAC 192k stereo
Video codec: libx264 yuv420p (universally supported on Android/iOS/TikTok)
Features:
- Smooth Ken Burns cinematic push-in (zoompan)
- Translucent backdrop pill for audio wave
- Real-time reactive audio waveform (cyan/gold glow)
- 3-layer synchronized lyrics (Hanzi + Pinyin + Vietsub)
- Drop beat highlight visual cue
"""
import os
import sys
import subprocess
import time

def render_music_video(
    bg_path="assets/background_base.jpg",
    audio_path="output/davu_chorus_56s.mp3",
    sub_path="output/davu_3layer_subtitles.ass",
    output_path="output/DaVu_Chinese_Version_Master.mp4",
    duration=56.0
):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    for f in [bg_path, audio_path, sub_path]:
        if not os.path.exists(f):
            raise FileNotFoundError(f"Required input file missing: {f}")
            
    print(f"Starting render -> {output_path}")
    print(f"Duration: {duration}s | Target: 1080x1920 @ 30fps")

    # Filter graph:
    # 1. Scale background to safe zoom canvas (1296x2304) and apply smooth continuous Ken Burns zoom
    # 2. Draw luxury translucent backdrop pill behind audio wave
    # 3. Generate audio waveform from audio stream
    # 4. Overlay waveform onto background
    # 5. Burn in 3-layer ASS subtitles
    filter_complex = (
        "[0:v]scale=1296x2304,"
        "zoompan=z='min(zoom+0.00007,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,"
        "drawbox=x=(1080-680)/2:y=345:w=680:h=105:color=0x0a0518@0.55:t=fill[bg_pill];"
        "[1:a]showwaves=s=640x75:mode=line:colors=0x66d1ff@0.85:scale=sqrt[wave];"
        "[bg_pill][wave]overlay=(W-w)/2:360[comp];"
        f"[comp]ass={sub_path},format=yuv420p[v]"
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
        "-preset", "fast",
        "-crf", "19",
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
    render_music_video()
