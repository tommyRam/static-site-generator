import unittest
from extract_title import extract_title

class ExtractTitleTest(unittest.TestCase):
    def test_extract_h1(self):
        res = extract_title("#heading1")
        self.assertEqual(res, "heading1")

    def test_extract_no_heading(self):
        res = extract_title("no heading")
        self.assertEqual(res, "no heading")

    def test_extract_h2(self):
        res = extract_title("## heading 2")
        self.assertEqual(res, "heading 2")

    def test_extract_h6_plus_extract_sharp(self):
        res = extract_title("####### heading 7")
        self.assertEqual(res, "# heading 7")

if __name__ == "__main__":
    unittest.main()