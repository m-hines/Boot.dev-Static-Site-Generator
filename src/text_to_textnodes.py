from split_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    node = [TextNode(text, TextType.PLAIN_TEXT)]
    node_split_first = split_nodes_delimiter(node, "**", TextType.BOLD_TEXT)
    node_split_second = split_nodes_delimiter(node_split_first, "_", TextType.ITALIC_TEXT)
    node_split_third = split_nodes_delimiter(node_split_second, "`", TextType.CODE_TEXT)
    node_split_fourth = split_nodes_image(node_split_third)
    node_split_fifth = split_nodes_link(node_split_fourth)
    return node_split_fifth
