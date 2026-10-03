import unittest
import os
import re

class TestSubtitles(unittest.TestCase):
    def setUp(self):
        self.ass_file = "output/davu_3layer_subtitles.ass"

    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.ass_file), f"{self.ass_file} must exist")

    def test_ass_structure(self):
        with open(self.ass_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Sections
        self.assertIn("[Script Info]", content)
        self.assertIn("[V4+ Styles]", content)
        self.assertIn("[Events]", content)

        # Resolution
        self.assertIn("PlayResX: 1080", content)
        self.assertIn("PlayResY: 1920", content)

        # Styles required
        for style in ["HeaderTitle", "HeaderArtist", "Hanzi", "Pinyin", "Vietsub", "DropHighlight"]:
            self.assertIn(f"Style: {style}", content, f"Missing style {style}")

        # Lyrics content check (all 6 viral lines)
        self.assertIn("树影灯影底随月影在摇晃", content)
        self.assertIn("慌的心中所想无处去隐藏", content)
        self.assertIn("勾勒出被遗忘的念念不忘", content)
        self.assertIn("冰凉的是否还能变滚烫", content)
        self.assertIn("谁翻云覆雨冷不防", content)
        self.assertIn("随风起舞 叹这长夜", content)

        # Dialogue count
        dialogues = re.findall(r"^Dialogue:\s*(\d+)", content, re.MULTILINE)
        self.assertGreaterEqual(len(dialogues), 20, "Should have at least 20 dialogue events")

if __name__ == "__main__":
    unittest.main()
