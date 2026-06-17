import re

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for block in blocks:
        if block:
            if re.match(r"```(?:([a-zA-Z0-9_\-+]+)?\n)?([\s\S]*?)\n?```", block.strip()):
                clean_blocks.append(block.removeprefix("\n"))
            else:
                # clean_blocks.append(block.replace("\n", " ").strip())
                clean_blocks.append(block.strip())

    return clean_blocks