import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextType, TextNode

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter_invalid_markdown(self):
        my_node = TextNode("this is **invalid markdown", TextType.PLAIN_TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([my_node], "**", TextType.BOLD_TEXT)
        
    def test_split_delimiter_italic_no_plain(self):
        my_node = TextNode("_this is italic text not plain text_", TextType.PLAIN_TEXT)
        split_node = split_nodes_delimiter([my_node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(split_node[0].text_type, TextType.ITALIC_TEXT)

    def test_split_delimiter_italic_some_plain(self):
        my_node = TextNode("this has _some plain_ text", TextType.PLAIN_TEXT)
        split_node = split_nodes_delimiter([my_node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(split_node[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(split_node[1].text_type, TextType.ITALIC_TEXT)
        self.assertEqual(split_node[2].text_type, TextType.PLAIN_TEXT)

    def test_split_delimiter_bold_some_plain(self):
        my_node = TextNode("this has bold text **at the end**", TextType.PLAIN_TEXT)
        split_node = split_nodes_delimiter([my_node], "**", TextType.BOLD_TEXT)
        self.assertEqual(split_node[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(split_node[1].text_type, TextType.BOLD_TEXT)

    def test_split_delimiter_for_empty_string(self):
        my_node = TextNode("this has ___too many_ delimiters", TextType.PLAIN_TEXT)
        split_node = split_nodes_delimiter([my_node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(split_node[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(split_node[1].text_type, TextType.ITALIC_TEXT)
        self.assertNotEqual(split_node[0].text, "")
        self.assertNotEqual(split_node[1].text, "")

