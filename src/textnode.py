from enum import Enum
from htmlnode import HTMLNode, LeafNode

class TextType(Enum):
    PLAIN_TEXT = "plain text"
    BOLD_TEXT = "bold text"
    ITALIC_TEXT = "italic text"
    CODE_TEXT = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            leaf_node = LeafNode(None, text_node.text)
            return leaf_node
        case TextType.BOLD_TEXT:
            leaf_node = LeafNode("b", text_node.text)
            return leaf_node
        case TextType.ITALIC_TEXT:
            leaf_node = LeafNode("i", text_node.text)
            return leaf_node
        case TextType.CODE_TEXT:
            leaf_node = LeafNode("code", text_node.text)
            return leaf_node
        case TextType.LINK:
            leaf_node = LeafNode("a", text_node.text, {"href": text_node.url})
            return leaf_node
        case TextType.IMAGE:
            leaf_node = LeafNode("img", "", {"src": "www.myimage.com", "alt": "what is alt text"})
            return leaf_node
        case _:
            raise ValueError("An invalid value was passed for text type.")
