#!/usr/bin/env python3
"""
Master Video Renderer for Dạ Vũ (夜舞) Chinese Version.
100% Real Live-Action Motion Footage of Ancient Chinese Beauties (Mỹ nhân Cổ Trang).
Zero watermarks, Zero static photos, Zero drop beat badges.
Full 200.088s duration synced with 3-layer ASS subtitles and studio audio.
"""
import os
import sys
import subprocess
import time

SOURCE_VIDEO = "assets/flower_goddesses_full.mp4"
AUDIO_FILE = "assets/davu_chinese_original.mp3"
PARTICLES_FILE = "assets/particles_loop.mp4"
SUBTITLES_FILE = "output/davu_full_subtitles.ass"
OVERLAY_FILE = "assets/cinematic_overlay.png"
OUTPUT_VIDEO = "output/DaVu_Chinese_Version_FULL_Master.mp4"
SEGS_DIR = "output/segments"

SEGMENTS = [
    # Act 1: Intro + Verse 1 (0:00 - 45.50s)
    {"id": "cut01", "ss": 0.0, "dur": 11.500, "desc": "Peach Blossom Goddess Intro Reveal"},
    {"id": "cut02", "ss": 11.5, "dur": 11.500, "desc": "Lotus Maiden Smiling & Head Turn"},
    {"id": "cut03", "ss": 23.0, "dur": 11.000, "desc": "Spring Maiden with Peach Branch (Verse 1)"},
    {"id": "cut04", "ss": 56.0, "dur": 11.500, "desc": "Emerald Silk Goddess Profile (Verse 1)"},
    
    # Act 2: Pre-Chorus 1 + Chorus 1 Drop Beat (45.50s - 98.00s)
    {"id": "cut05", "ss": 64.0, "dur": 12.500, "desc": "Waving Sleeves Maiden (Pre-Chorus 1)"},
    {"id": "cut06", "ss": 28.0, "dur": 15.000, "desc": "Walking Blossom Maiden (Pre-Chorus 1)"},
    {"id": "cut07", "ss": 75.0, "dur": 12.500, "desc": "Golden Peony Goddess Dance (Drop Beat 1)"},
    {"id": "cut08", "ss": 77.4, "dur": 12.500, "desc": "Golden Goddess Climax Twirl (Drop Beat 1)"},
    
    # Act 3: Guzheng Solo + Verse 2 + Pre-Chorus 2 (98.00s - 146.00s)
    {"id": "cut09", "ss": 13.0, "dur": 11.000, "desc": "Lotus Maiden Interlude (Guzheng Solo)"},
    {"id": "cut10", "ss": 58.0, "dur": 12.500, "desc": "Emerald Goddess Emotional Gaze (Verse 2)"},
    {"id": "cut11", "ss": 25.0, "dur": 12.500, "desc": "Spring Maiden Breeze Turn (Verse 2)"},
    {"id": "cut12", "ss": 66.0, "dur": 12.000, "desc": "Poetic Maiden Glance (Pre-Chorus 2)"},
    
    # Act 4: Chorus 2 Drop Beat + Outro (146.00s - 200.088s)
    {"id": "cut13", "ss": 74.5, "dur": 14.000, "desc": "Grand Peony Dance Climax (Drop Beat 2)"},
    {"id": "cut14", "ss": 76.0, "dur": 13.000, "desc": "Dancing Twirl Climax (Drop Beat 2 Peak)"},
    {"id": "cut15", "ss": 14.0, "dur": 13.500, "desc": "Lotus Maiden Soft Sway (Outro Part 1)"},
    {"id": "cut16", "ss": 1.5, "dur": 13.588, "desc": "Peach Blossom Goddess Sunset Farewell (Outro)"},
]

def render_segment(seg):
    seg_id = seg["id"]
    ss = seg["ss"]
    dur = seg["dur"]
    out_file = os.path.join(SEGS_DIR, f"{seg_id}.mp4")
    
    vf = "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920:flags=lanczos,fps=30,format=yuv420p"
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(ss),
        "-t", str(dur),
        "-i", SOURCE_VIDEO,
        "-vf", vf,
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-threads", "4",
        "-t", str(dur),
        out_file
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  [OK] Rendered {seg_id}: {seg['desc']} ({dur:.3f}s)")
    return out_file

def main():
    total_start = time.time()
    os.makedirs(SEGS_DIR, exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    total_dur = sum(s["dur"] for s in SEGMENTS)
    print(f"=== Rendering Real Live-Action Motion Video for Dạ Vũ ===")
    print(f"Total target duration: {total_dur:.3f}s across {len(SEGMENTS)} dynamic scenes")
    
    # Step 1: Render all 16 segments
    seg_files = []
    print("\n--- Step 1/3: Rendering individual 9:16 vertical cuts ---")
    for i, seg in enumerate(SEGMENTS):
        t0 = time.time()
        sf = render_segment(seg)
        seg_files.append(sf)
        print(f"       -> Done in {time.time()-t0:.2f}s")
        
    # Step 2: Concat all segments
    print("\n--- Step 2/3: Concatenating all scenes ---")
    concat_list = os.path.join(SEGS_DIR, "live_concat_list.txt")
    with open(concat_list, "w") as f:
        for sf in seg_files:
            f.write(f"file '{os.path.abspath(sf)}'\n")
            
    concat_video = os.path.join(SEGS_DIR, "concatenated_live_scenes.mp4")
    cmd_concat = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list,
        "-c", "copy",
        concat_video
    ]
    subprocess.run(cmd_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  [OK] Concatenated video ready: {concat_video}")
    
    # Step 3: Composite final master
    print("\n--- Step 3/3: Final Compositing (Particles + Subtitles + Audio) ---")
    # Stream 0: concatenated live video (200.088s)
    # Stream 1: particles loop (stream_loop)
    # Stream 2: cinematic overlay (vignette)
    # Stream 3: audio
    filter_complex = (
        "[1:v]colorkey=0x000000:0.12:0.08[pt];"
        "[0:v][pt]overlay=0:0:shortest=1[with_pt];"
        "[with_pt][2:v]overlay=0:0[with_vignette];"
        f"[with_vignette]ass={SUBTITLES_FILE},format=yuv420p[outv]"
    )
    
    final_cmd = [
        "ffmpeg", "-y",
        "-i", concat_video,
        "-stream_loop", "-1", "-i", PARTICLES_FILE,
        "-loop", "1", "-i", OVERLAY_FILE,
        "-i", AUDIO_FILE,
        "-filter_complex", filter_complex,
        "-map", "[outv]",
        "-map", "3:a",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "19",
        "-c:a", "aac",
        "-b:a", "320k",
        "-t", f"{total_dur:.3f}",
        "-threads", "4",
        OUTPUT_VIDEO
    ]
    print("  Executing final master compositing...")
    subprocess.run(final_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    elapsed = time.time() - total_start
    print(f"\n=== SUCCESS! Master Video Finished in {elapsed:.1f}s ===")
    print(f"Output File: {OUTPUT_VIDEO}")
    
    # Check output size
    if os.path.exists(OUTPUT_VIDEO):
        sz = os.path.getsize(OUTPUT_VIDEO) / (1024 * 1024)
        print(f"File Size: {sz:.2f} MB")

if __name__ == "__main__":
    main()
