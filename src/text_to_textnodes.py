from textnode import TextType, TextNode
from splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text) -> list[TextNode]:
    delimiters = ["**", "_", "`"]
    types = [TextType.BOLD, TextType.ITALIC, TextType.CODE]
    nodes = [TextNode(text, TextType.TEXT)]

    for i, delimiter in enumerate(delimiters):
        nodes = split_nodes_delimiter(nodes, delimiter, types[i])
        # print(f"after delimiter: {delimiter} we got: {nodes}")

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

if __name__ == "__main__":
    # text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    # text = "<li>An elaborate pantheon of deities (the `Valar` and `Maiar`)</li><li>The tragic saga of the Noldor Elves</li><li>The rise and fall of great kingdoms such as Gondolin and Númenor</li>"
    text = "_An unpopular opinion, I know_"
    ans = text_to_textnodes(text)
    print(ans)