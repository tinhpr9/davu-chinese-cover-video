import unittest
import os
import subprocess
import json

class TestAudio(unittest.TestCase):
    def setUp(self):
        self.audio_file = "output/davu_chorus_56s.mp3"

    def test_audio_exists(self):
        self.assertTrue(os.path.exists(self.audio_file), f"{self.audio_file} should exist")
        self.assertGreater(os.path.getsize(self.audio_file), 100000, "Audio file size should be > 100KB")

    def test_audio_properties(self):
        cmd = [
            "ffprobe", "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            self.audio_file
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "ffprobe should succeed")
        data = json.loads(result.stdout)
        
        # Duration check (~56s)
        duration = float(data["format"]["duration"])
        self.assertAlmostEqual(duration, 56.0, delta=1.0, msg="Duration should be approx 56 seconds")

        # Stream checks
        streams = data["streams"]
        self.assertGreater(len(streams), 0, "Should have at least 1 audio stream")
        audio_stream = streams[0]
        self.assertEqual(audio_stream["codec_name"], "mp3")
        self.assertEqual(int(audio_stream["sample_rate"]), 44100)
        self.assertEqual(int(audio_stream["channels"]), 2)

if __name__ == "__main__":
    unittest.main()
