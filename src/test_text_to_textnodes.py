import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):

    def test_text_to_textnodes(self):
        testnode1 = TextNode("Some **markdown** with _various_ delimiters including `code`. Here is an image: ![my image here](www.myimage.jpeg). We also have a link: [my link here](www.mylink.com). Ending with more plain text.", TextType.PLAIN_TEXT)
        my_nodes_list = text_to_textnodes(testnode1.text)
        testnode2 = TextNode("Some ", TextType.PLAIN_TEXT)
        testnode3 = TextNode("markdown", TextType.BOLD_TEXT)
        testnode4 = TextNode(" with ", TextType.PLAIN_TEXT)
        testnode5 = TextNode("various", TextType.ITALIC_TEXT)
        testnode6 = TextNode(" delimiters including ", TextType.PLAIN_TEXT)
        testnode7 = TextNode("code", TextType.CODE_TEXT)
        testnode8 = TextNode(". Here is an image: ", TextType.PLAIN_TEXT)
        testnode9 = TextNode("my image here", TextType.IMAGE, "www.myimage.jpeg")
        testnode10 = TextNode(". We also have a link: ", TextType.PLAIN_TEXT)
        testnode11 = TextNode("my link here", TextType.LINK, "www.mylink.com")
        testnode12 = TextNode(". Ending with more plain text.", TextType.PLAIN_TEXT)
        self.assertListEqual(my_nodes_list, [testnode2, testnode3, testnode4, testnode5, testnode6, testnode7, testnode8, testnode9, testnode10, testnode11, testnode12])
