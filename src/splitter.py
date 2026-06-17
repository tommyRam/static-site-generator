import copy
from textnode import TextNode, TextType

from markdown import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(
        old_nodes: list[TextNode], 
        delimiter: str, 
        text_type: TextType
) -> list[TextNode]:
    splitted_nodes: list[TextNode] = []

    for old_node in old_nodes:
        # if old_node.text_type == TextType.TEXT:
        #     splitted_nodes.append(copy.deepcopy(old_node))
        # else:
        left = old_node.text.find(delimiter)
        right = old_node.text.rfind(delimiter)

        if left == -1 or right == -1:
            splitted_nodes.append(copy.deepcopy(old_node))
            continue
        if left == right:
            raise Exception(f"Error: TextNode not well formatted for {old_node.text}")

        splitted = old_node.text.split(delimiter)
        new_splitted = []

        for spl in splitted:
            if spl:
                new_splitted.append(spl)

        splitted = new_splitted
        # print(f"splitted: {splitted}")

        if len(splitted) == 0:
            splitted_nodes.append(copy.deepcopy(old_node))
        elif len(splitted) == 1:
            splitted_nodes.append(TextNode(splitted[0], text_type))
        elif len(splitted) == 2:
            if left == 0:
                splitted_nodes.extend([
                    TextNode(splitted[0], text_type),
                    TextNode(splitted[1], TextType.TEXT)
                ])
            else:
                splitted_nodes.extend([
                    TextNode(splitted[0], TextType.TEXT),
                    TextNode(splitted[1], text_type)
                ])
        elif len(splitted) > 2:
            splitted_nodes.extend([
                TextNode(splitted[0], TextType.TEXT),
                TextNode(splitted[1], text_type),
                # TextNode(splitted[2], TextType.TEXT)
            ])
            # splitted_nodes.extend(
            #     split_nodes_delimiter([TextNode(splitted[0], TextType.TEXT), TextNode(splitted[1], TextType.TEXT), TextNode(splitted[2], TextType.TEXT)], delimiter, text_type)
            # )
            from_index = len(splitted[0]) + len(splitted[1]) + (len(delimiter) * 2)
            new_text_node = TextNode(old_node.text[from_index:], TextType.TEXT)
            # print(new_text_node)
            splitted_nodes.extend(
                split_nodes_delimiter([new_text_node], delimiter, text_type)
            )
    return splitted_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    splitted_nodes: list[TextNode] = []

    for old_node in old_nodes:
        markdown_images = extract_markdown_images(old_node.text)

        if len(markdown_images) == 0:
            splitted_nodes.append(copy.deepcopy(old_node))
            continue
        else:
            text = old_node.text
            for markdown_image in markdown_images:
                current_separator = f"![{markdown_image[0]}]({markdown_image[1]})"
                splitted = text.split(current_separator)

                if len(splitted) == 0:
                    splitted_nodes.append(TextNode(markdown_image[0], TextType.IMAGE, markdown_image[1]))
                    text = ""
                elif len(splitted) == 2:
                    if splitted[0]:
                        splitted_nodes.extend([
                            TextNode(splitted[0], TextType.TEXT),
                            TextNode(markdown_image[0], TextType.IMAGE, markdown_image[1])
                        ])
                    else:
                        splitted_nodes.append(TextNode(markdown_image[0], TextType.IMAGE, markdown_image[1]))
                    text = splitted[1]
            if text:
                splitted_nodes.append(TextNode(text, TextType.TEXT))
    return splitted_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    splitted_nodes: list[TextNode] = []

    for old_node in old_nodes:
        markdown_links = extract_markdown_links(old_node.text)

        if len(markdown_links) == 0:
            splitted_nodes.append(copy.deepcopy(old_node))
            continue
        else:
            text = old_node.text
            for markdown_link in markdown_links:
                current_separator = f"[{markdown_link[0]}]({markdown_link[1]})"
                splitted = text.split(current_separator)

                if len(splitted) == 0:
                    splitted_nodes.append(TextNode(markdown_link[0], TextType.LINK, markdown_link[1]))
                    text = ""
                elif len(splitted) == 2:
                    if splitted[0]:
                        splitted_nodes.extend([
                            TextNode(splitted[0], TextType.TEXT),
                            TextNode(markdown_link[0], TextType.LINK, markdown_link[1])
                        ])
                    else:
                        splitted_nodes.append(TextNode(markdown_link[0], TextType.LINK, markdown_link[1]))
                    text = splitted[1]
            if text:
                splitted_nodes.append(TextNode(text, TextType.TEXT))
    return splitted_nodes


if __name__ == "__main__":
    node = TextNode("This is **text** with an _italic_", TextType.TEXT)
    ans = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(ans)


