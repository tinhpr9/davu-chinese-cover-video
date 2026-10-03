import unittest
import os
import subprocess
import json

class TestVideo(unittest.TestCase):
    def setUp(self):
        self.video_file = "output/DaVu_Chinese_Version_Master.mp4"

    def test_video_exists_and_size(self):
        self.assertTrue(os.path.exists(self.video_file), f"{self.video_file} must exist")
        # 56s 1080x1920 video should be at least 3MB
        file_size = os.path.getsize(self.video_file)
        self.assertGreater(file_size, 3 * 1024 * 1024, "Video should be at least 3MB")

    def test_video_stream_properties(self):
        cmd = [
            "ffprobe", "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            self.video_file
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "ffprobe should succeed")
        data = json.loads(result.stdout)

        # Duration check (~56s)
        duration = float(data["format"]["duration"])
        self.assertAlmostEqual(duration, 56.0, delta=1.5, msg="Video duration should be approx 56 seconds")

        # Stream verification
        video_stream = None
        audio_stream = None
        for stream in data["streams"]:
            if stream["codec_type"] == "video":
                video_stream = stream
            elif stream["codec_type"] == "audio":
                audio_stream = stream

        self.assertIsNotNone(video_stream, "Video stream missing")
        self.assertIsNotNone(audio_stream, "Audio stream missing")

        # Video dimensions: 1080x1920
        self.assertEqual(video_stream["width"], 1080)
        self.assertEqual(video_stream["height"], 1920)
        self.assertEqual(video_stream["codec_name"], "h264")
        self.assertIn(video_stream["pix_fmt"], ["yuv420p", "yuvj420p"])

        # Audio stream
        self.assertEqual(audio_stream["codec_name"], "aac")
        self.assertEqual(int(audio_stream["sample_rate"]), 44100)
        self.assertEqual(int(audio_stream["channels"]), 2)

if __name__ == "__main__":
    unittest.main()
