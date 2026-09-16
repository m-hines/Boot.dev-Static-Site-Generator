import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node1, node2)

    def test_if_both_are_italic(self):
        node1 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertEqual(node1, node2)

    def test_if_both_are_code(self):
        node1 = TextNode("This is a text node", TextType.CODE_TEXT)
        node2 = TextNode("This is a text node", TextType.CODE_TEXT)
        self.assertEqual(node1, node2)
    
    def test_if_both_are_not_italic(self):
        node1 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node1, node2)

    def test_if_nodes_have_different_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This node has different text", TextType.BOLD_TEXT)
        self.assertNotEqual(node1, node2)

    def text_if_both_have_same_url(self):
        node1 = TextNode("This is a text node", TextType.CODE_TEXT, url="www.red.com")
        node2 = TextNode("This is a text node", TextType.CODE_TExT, url="www.red.com")
        self.assertEqual(node1, node2)

    def text_if_different_url(self):
        node1 = TextNode("This is a text node", TextType.CODE_TEXT, url="www.red.com")
        node2 = TextNode("This is a text node", TextType.CODE_TExT, url="www.blue.com")
        self.assertNotEqual(node1, node2)

    def test_node_to_html_node_no_tag(self):
        text_node = TextNode("some raw text", TextType.PLAIN_TEXT)
        html_text_node = text_node_to_html_node(text_node)
        self.assertEqual(html_text_node.value, "some raw text")

    def test_node_to_html_node_bold(self):
        text_node = TextNode("bold text", TextType.BOLD_TEXT)
        html_text_node = text_node_to_html_node(text_node)
        self.assertEqual(html_text_node.tag, "b")
        self.assertEqual(html_text_node.value, "bold text")

    def test_node_to_html_node_italic(self):
        text_node = TextNode("italic text", TextType.ITALIC_TEXT)
        html_text_node = text_node_to_html_node(text_node)
        self.assertEqual(html_text_node.tag, "i")
        self.assertEqual(html_text_node.value, "italic text")

    def test_node_to_html_node_code(self):
        text_node = TextNode("code text", TextType.CODE_TEXT)
        html_text_node = text_node_to_html_node(text_node)
        self.assertEqual(html_text_node.tag, "code")
        self.assertEqual(html_text_node.value, "code text")

    def test_node_to_html_node_anchor(self):
        text_node = TextNode("anchor text", TextType.LINK, "www.electronicgems.com")
        html_text_node = text_node_to_html_node(text_node)
        self.assertEqual(html_text_node.tag, "a")
        self.assertEqual(html_text_node.value, "anchor text")
        self.assertEqual(html_text_node.props["href"], "www.electronicgems.com")

    def test_node_to_html_node_invalid_texttype(self):
        text_node = TextNode("some text", None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()
