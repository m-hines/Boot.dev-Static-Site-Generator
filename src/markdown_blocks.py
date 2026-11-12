from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(markdown_block):
    split_list = markdown_block.split("\n")
    if markdown_block[:2] == "# " or markdown_block[:3] == "## " or markdown_block[:4] == "### " or markdown_block[:5] == "#### " or markdown_block[:6] == "##### " or markdown_block[:7] == "###### ":
        return BlockType.HEADING
    if split_list[0] == "```" and split_list[-1] == "```" and len(split_list) >= 3:
        return BlockType.CODE
    if all(line.startswith(">") for line in split_list):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in split_list):
        return BlockType.UNORDERED_LIST
    for number, line in enumerate(split_list, start=1):
        prefix = f"{number}. "
        if line.startswith(prefix) is False:
            return BlockType.PARAGRAPH
    return BlockType.ORDERED_LIST
