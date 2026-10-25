from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    if markdown[0] == "#":
        return BlockType.HEADING
    if markdown[0] == "```\n":
        return BlockType.CODE
    if markdown[0] == ">":
        return BlockType.QUOTE
    if markdown[0] == 