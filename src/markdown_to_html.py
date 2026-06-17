import re
from markdown_to_blocks import markdown_to_blocks
from block import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import HTMLNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    # print(f"blocks: {blocks}")
    html_code = ""

    for block in blocks:
        block_type = block_to_block_type(block)
        block_html_tag = get_html_tag_from_block_type(block_type)

        # print(f"current block: {block}")
        # print(f"blocktype: {block_type}\n\n")

        new_htmlnode = HTMLNode(block_html_tag, "")
        cleaned_block_text = remove_special_markdown_text(block_type, block)

        if block_html_tag == "code":
            html_code += f"<pre><{block_html_tag}>{cleaned_block_text}</{block_html_tag}></pre>"
            continue

        text_nodes = text_to_textnodes(cleaned_block_text)

        # if block_html_tag == "ol":
        #     print(f"cleaneeeeeeeeeeeee: {cleaned_block_text}")
        #     print(f"textnodes: {text_nodes}")

        child_htmlnodes = []
        for text_node in text_nodes:
            # print(f"textnodeeeeeeee: {text_node}")
            child_htmlnodes.append(text_node_to_html_node(text_node))

        # print(f"childdddddd: {child_htmlnodes}")
        new_htmlnode.children = child_htmlnodes

        # if block_html_tag == "ol":
            # print(f"chilllllllllllllL: {child_htmlnodes}")

        html_code += f"<{block_html_tag}>"
        for child in child_htmlnodes:
            if child.value != None:
                html_code += child.to_html()

        html_code += f"</{block_html_tag}>"
    return HTMLNode(value=html_code)

def get_html_tag_from_block_type(block_type: BlockType):
    if block_type == BlockType.HEADING:
        return "h1"
    elif block_type == BlockType.CODE:
        return "code"
    elif block_type == BlockType.QUOTE:
        return "blockquote"
    elif block_type == BlockType.UNORDERED_LIST:
        return "ul"
    elif block_type == BlockType.ORDERED_LIST:
        return "ol"
    else:
        return "p"
    
def remove_special_markdown_text(block_type: BlockType, block_text: str) -> str:
    if block_type == BlockType.HEADING:
        return remove_heading_markdown(block_text)
    if block_type == BlockType.CODE:
        return remove_code_markdown_symbol(block_text)
    if block_type == BlockType.QUOTE:
        return remove_quote_markdown_symbol(block_text)
    if block_type == BlockType.UNORDERED_LIST:
        return remove_unordered_list_markdown_symbol(block_text)
    if block_type == BlockType.ORDERED_LIST:
        return remove_ordered_list_markdown_symbol(block_text)
    
    return block_text

def remove_heading_markdown(text: str) -> str:
    i = 0
    while i < len(text) and text[i] == "#" and i < 6:
        i += 1
    return text[i:].strip()

def remove_code_markdown_symbol(text: str) -> str:
    res =  text.removeprefix("```").strip().removesuffix("```")
    return res

def remove_quote_markdown_symbol(text: str) -> str:
    return text.removeprefix(">").strip()

def remove_unordered_list_markdown_symbol(text: str) -> str:
    # print(f"heeeeeeeeeeeeeeeeeeeee: {text}")
    return format_list(text, "-")

def remove_ordered_list_markdown_symbol(text: str) -> str:
    # print(f"heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee: {text}")
    formatted =  format_list(text, ".")
    # print(formatted)
    return formatted

def format_list(text: str, splitter: str) -> str:
    texts = text.split("\n")
    formatted_ordered_list = ""

    for t in texts:
        formatted_ordered_list += f"<li>{t.split(splitter)[1].strip()}</li>"

    # print(f"formateddddddddd: {formatted_ordered_list}")
    return formatted_ordered_list

if __name__ == "__main__":
#     md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    ans = markdown_to_html_node(md)
    print(ans)