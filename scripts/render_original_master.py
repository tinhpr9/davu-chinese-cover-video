#!/usr/bin/env python3
"""
Master Video Renderer for Dạ Vũ (夜舞) Chinese Version - 100% Original Multi-Scene Visual.
Features:
- 100% Original AI Artwork (Zero stolen content, Zero watermarks)
- 4 Distinct Ancient Chinese Scenes matching song narrative:
  * Scene 1 (0:00 - 45.5s): Pipa maiden under lantern pavilion (Intro & Verse 1)
  * Scene 2 (45.5s - 98.0s): Silk dance maiden under full moon (Pre-Chorus 1 & Drop 1)
  * Scene 3 (98.0s - 146.0s): Guzheng maiden by lotus pond (Solo & Verse 2)
  * Scene 4 (146.0s - 200.088s): Crimson fan maiden under festival lanterns (Drop 2 & Outro)
- Continuous Ken Burns camera motion on all 4 scenes
- Dynamic particle VFX (Cherry blossom petals & gentle snow drift)
- Clean 3-layer ASS subtitles (Hanzi + Pinyin + Vietsub) with NO green badges
- Studio audio (Hoàng Linh - 黄龄 × Tăng Duy Tân)
"""
import os
import sys
import subprocess
import time

def render_segment(img_path, duration, out_path, zoom_expr="min(zoom+0.00004,1.06)", x_expr="iw/2-(iw/zoom/2)", y_expr="ih/3-(ih/zoom/3)"):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    filter_str = f"scale=1200:2134,zoompan=z='{zoom_expr}':x='{x_expr}':y='{y_expr}':d=1:s=1080x1920:fps=30,format=yuv420p"
    cmd = [
        "ffmpeg", "-y",
        "-framerate", "30",
        "-loop", "1",
        "-t", str(duration),
        "-i", img_path,
        "-vf", filter_str,
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-t", str(duration),
        out_path
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"Segment rendered: {out_path} ({duration}s)")
    return out_path

def render_original_master(
    output_path="output/DaVu_Chinese_Version_FULL_Master.mp4",
    total_duration=200.088
):
    start_time = time.time()
    os.makedirs("output/segments", exist_ok=True)
    
    # 4 Scenes definitions
    scenes = [
        ("assets/chinese_beauty_pipa.jpg", 45.50, "output/segments/seg1.mp4", "min(zoom+0.00004,1.06)", "iw/2-(iw/zoom/2)", "ih/3-(ih/zoom/3)"),
        ("assets/chinese_beauty_silk_dance.jpg", 52.50, "output/segments/seg2.mp4", "min(zoom+0.00003,1.05)", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"),
        ("assets/chinese_beauty_guzheng.jpg", 48.00, "output/segments/seg3.mp4", "min(zoom+0.00004,1.06)", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"),
        ("assets/chinese_beauty_blossom_fan.jpg", 54.088, "output/segments/seg4.mp4", "min(zoom+0.00004,1.06)", "iw/2-(iw/zoom/2)", "ih/3-(ih/zoom/3)")
    ]

    print("Step 1: Rendering 4 distinct scene segments with Ken Burns dynamic motion...")
    seg_files = []
    for img, dur, seg_out, z_e, x_e, y_e in scenes:
        render_segment(img, dur, seg_out, z_e, x_e, y_e)
        seg_files.append(seg_out)

    # Concat list file
    concat_list_path = "output/segments/concat_list.txt"
    with open(concat_list_path, "w") as f:
        for sf in seg_files:
            abs_sf = os.path.abspath(sf)
            f.write(f"file '{abs_sf}'\n")

    print("Step 2: Concatenating scene segments...")
    concat_video = "output/segments/concatenated_scenes.mp4"
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        concat_video
    ], check=True, capture_output=True)

    print("Step 3: Final Compositing with Blossom/Snow Particles, Gradient Vignette & Clean Subtitles...")
    particles_path = "assets/particles_loop.mp4"
    overlay_path = "assets/cinematic_overlay.png"
    audio_path = "assets/davu_chinese_original.mp3"
    sub_path = "output/davu_full_subtitles.ass"

    # Filter graph:
    # 0:v = concatenated scenes (200.088s)
    # 1:v = looping particles
    # 2:v = cinematic gradient overlay
    filter_complex = (
        "[1:v]colorkey=0x000000:0.12:0.08[pt];"
        "[0:v][pt]overlay=0:0:shortest=1[with_pt];"
        "[with_pt][2:v]overlay=0:0[with_vignette];"
        f"[with_vignette]ass={sub_path},format=yuv420p[outv]"
    )

    final_cmd = [
        "ffmpeg", "-y",
        "-i", concat_video,
        "-stream_loop", "-1", "-i", particles_path,
        "-i", overlay_path,
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[outv]",
        "-map", "3:a",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-t", str(total_duration),
        output_path
    ]

    subprocess.run(final_cmd, check=True)
    elapsed = time.time() - start_time
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\n Master Video Render Completed in {elapsed:.1f}s!")
    print(f"Output: {output_path} ({size_mb:.2f} MB)")
    return output_path

if __name__ == "__main__":
    render_original_master()
