import unittest
from block import block_to_block_type, BlockType

class TestBlock(unittest.TestCase):
    def test_heading(self):
        block_type = block_to_block_type("## heading")
        self.assertEqual(block_type, BlockType.HEADING)

    def test_quote(self):
        block_type = block_to_block_type(">quote text")
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_list(self):
        block_type = block_to_block_type("- unordered")
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block_type = block_to_block_type("1. ordered")
        self.assertEqual(block_type, BlockType.ORDERED_LIST)
    
    def test_paragraph(self):
        block_type = block_to_block_type("simple paragraph")
        self.assertEqual(block_type, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()