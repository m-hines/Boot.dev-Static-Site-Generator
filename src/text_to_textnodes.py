from split_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    nodes_list = [TextNode(text, TextType.PLAIN_TEXT)]
    nodes_list_split_delimiter = split_delimiter(textnodes_list)
    nodes_list_split_nodes = split_nodes(nodes_list_split_delimiter)
    return nodes_list_split_nodes
