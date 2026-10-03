import unittest
import os
import subprocess
import json

class TestFullVideo(unittest.TestCase):
    def setUp(self):
        self.sub_file = "output/davu_full_subtitles.ass"
        self.video_file = "output/DaVu_Chinese_Version_FULL_Master.mp4"

    def test_full_subtitles_structure(self):
        self.assertTrue(os.path.exists(self.sub_file), "Full subtitles file must exist")
        with open(self.sub_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Check required sections
        self.assertIn("[Script Info]", content)
        self.assertIn("PlayResX: 1080", content)
        self.assertIn("PlayResY: 1920", content)

        # Check key full song lyrics
        self.assertIn("恰好照在夜风微凉的晚上", content)
        self.assertIn("树影灯影都随月影在摇晃", content)
        self.assertIn("晃得心中所想无处去隐藏", content)
        self.assertIn("都怪我还想 沉溺于你的假象", content)
        self.assertIn("就让回忆随时间流淌 可前路悠长", content)
        self.assertIn("随风起舞 叹这长夜", content)

    def test_full_video_properties(self):
        if not os.path.exists(self.video_file):
            self.skipTest(f"{self.video_file} not rendered yet")

        cmd = [
            "ffprobe", "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            self.video_file
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)

        # Full duration check (~200s)
        duration = float(data["format"]["duration"])
        self.assertAlmostEqual(duration, 200.0, delta=2.0)

        # Streams check
        v_stream = next(s for s in data["streams"] if s["codec_type"] == "video")
        a_stream = next(s for s in data["streams"] if s["codec_type"] == "audio")

        self.assertEqual(v_stream["width"], 1080)
        self.assertEqual(v_stream["height"], 1920)
        self.assertEqual(v_stream["codec_name"], "h264")
        self.assertIn(v_stream["pix_fmt"], ["yuv420p", "yuvj420p"])

        self.assertEqual(a_stream["codec_name"], "aac")

if __name__ == "__main__":
    unittest.main()
