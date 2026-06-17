import unittest
from textnode import TextNode, TextType
from splitter import split_nodes_image

class SplitterImageTest(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_no_image(self):
        node = TextNode(
            "This is a text without an image", 
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text without an image", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_images_image_in_the_beginning(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png): this is the image",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(": this is the image", TextType.TEXT)
            ],
            new_nodes
        )
    
    def test_split_images_in_the_end(self):
        node = TextNode(
            "This is the image: ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is the image: ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes
        )

    def test_split_images_only(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes
        )

    def test_split_images_two_images_separated_by_space(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()