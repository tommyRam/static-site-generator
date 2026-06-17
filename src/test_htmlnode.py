import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def to_html_raise_not_implemented(self):
        node = HTMLNode("p", "Test paragraph", None, {"class": "paragra-class"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode("p", "Test paragraph", None, {"class": "paragra-class", "target": "_blank"})
        excepted_props_to_html = 'class="paragra-class" target="_blank"'

        self.assertEqual(node.props_to_html(), excepted_props_to_html)

    def test_propt_to_hmtl_empty(self):
        node = HTMLNode("p", "Test paragraph")
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()