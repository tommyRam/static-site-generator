import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children_with_props(self):
        child_node = LeafNode("span", "child", {"class": "child-class"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><span class="child-class">child</span></div>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_raise_not_parent_tag(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode(None, [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()