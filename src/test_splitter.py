"""
Case 1: Hello **world**!
Case 2: **Hello world**
Case 3: Hello **world**
Case 4: **Hello** world
"""
import unittest
from textnode import TextNode, TextType
from splitter import split_nodes_delimiter

class TestSplitter(unittest.TestCase):
    def test_simple_text(self):
        simple_text = TextNode("Hello world", TextType.TEXT)
        splitted_nodes = split_nodes_delimiter([simple_text], "**", TextType.BOLD)
        self.assertEqual(splitted_nodes[0], TextNode("Hello world", TextType.TEXT))

    def test_raise_exception_for_input_not_well_formatted(self):
        not_formatted_text_node = TextNode("Hello ** World", TextType.BOLD)

        with self.assertRaises(Exception):
            split_nodes_delimiter([not_formatted_text_node], "**", TextType.BOLD)

    def test_splitted_into_three_textnode_ok(self):
        text_node = TextNode("Hello **world** !", TextType.BOLD)
        splitted_nodes = split_nodes_delimiter([text_node], "**", TextType.BOLD)
        self.assertEqual(len(splitted_nodes), 3)

if __name__ == "__main__":
    unittest.main()