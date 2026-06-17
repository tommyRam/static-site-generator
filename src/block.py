from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if re.match(r"^(#{1,6})\s+(.+)$", block):
        return BlockType.HEADING
    elif re.match(r"```(?:([a-zA-Z0-9_\-+]+)?\n)?([\s\S]*?)\n?```", block):
        return BlockType.CODE
    elif all(re.match(r'^>\s*(.*)$', line) for line in block.split("\n")):
        return BlockType.QUOTE
    elif all(re.match(r"^\s*[-+*]\s+(.+)$", line) for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    elif re.match(r"^\s*\d+\.\s+(.*)", block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
if __name__ ==  "__main__":
    print(block_to_block_type("```code\n```"))