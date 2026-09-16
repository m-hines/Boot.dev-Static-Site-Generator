from inline_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):   # returns a list of TextNodes
    node_list = []
    for node in old_nodes:
        original_text = node.text
        split_image = extract_markdown_images(node.text)
        for i in split_image:
            delimiter = f"![{i[0]}]({i[1]})"
            sections = original_text.split(delimiter, 1)
            if sections[0] != "":
                new_plain_node = TextNode(sections[0], TextType.PLAIN_TEXT)
                node_list.append(new_plain_node)
            new_image_node = TextNode(i[0], TextType.IMAGE, i[1])
            node_list.append(new_image_node)
            original_text = sections[1]
        if len(original_text) > 0:
            new_plain_node = TextNode(original_text, TextType.PLAIN_TEXT)
            node_list.append(new_plain_node)
    return node_list

def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
        original_text = node.text
        split_link = extract_markdown_links(node.text)
        for i in split_link:
            delimiter = f"[{i[0]}]({i[1]})"
            sections = original_text.split(delimiter, 1)
            if sections[0] != "":
                new_plain_node = TextNode(sections[0], TextType.PLAIN_TEXT)
                node_list.append(new_plain_node)
            new_link_node = TextNode(i[0], TextType.LINK, i[1])
            node_list.append(new_link_node)
            original_text = sections[1]
        if len(original_text) > 0:
            new_plain_node = TextNode(original_text, TextType.PLAIN_TEXT)
            node_list.append(new_plain_node)
    return node_list

# consider edge cases (see Boot's last comment in Split Images and Links)