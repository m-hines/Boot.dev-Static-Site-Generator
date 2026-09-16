import unittest
from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):

    def test_split_images_multiple(self):
        test_node1 = TextNode("Some test text with image. ![smiley face](www.smiley.jpeg) That's a pretty smile!", TextType.PLAIN_TEXT)
        test_node2 = TextNode("More testing of image. ![silly face](www.silly_face.png) What so silly?", TextType.PLAIN_TEXT)
        my_list = split_nodes_image([test_node1, test_node2])
        test_node3 = TextNode("Some test text with image. ", TextType.PLAIN_TEXT)
        test_node4 = TextNode("smiley face", TextType.IMAGE, "www.smiley.jpeg")
        test_node5 = TextNode(" That's a pretty smile!", TextType.PLAIN_TEXT)
        test_node6 = TextNode("More testing of image. ", TextType.PLAIN_TEXT)
        test_node7 = TextNode("silly face", TextType.IMAGE, "www.silly_face.png")
        test_node8 = TextNode(" What so silly?", TextType.PLAIN_TEXT)
        self.assertListEqual(my_list, [test_node3, test_node4, test_node5, test_node6, test_node7, test_node8])

    def test_split_images_beginning(self):
        test_node1 = TextNode("![image beginning](www.my_image.jpeg) The image is first.", TextType.PLAIN_TEXT)
        my_list = split_nodes_image([test_node1])
        test_node2 = TextNode("image beginning", TextType.IMAGE, "www.my_image.jpeg")
        test_node3 = TextNode(" The image is first.", TextType.PLAIN_TEXT)
        self.assertListEqual(my_list, [test_node2, test_node3])

    def test_split_images_end(self):
        test_node1 = TextNode("Image is at end. ![end image](www.end_image.jpeg)", TextType.PLAIN_TEXT)
        my_list = split_nodes_image([test_node1])
        test_node2 = TextNode("Image is at end. ", TextType.PLAIN_TEXT)
        test_node3 = TextNode("end image", TextType.IMAGE, "www.end_image.jpeg")
        self.assertListEqual(my_list, [test_node2, test_node3])

    def test_split_images_no_image(self):
        test_node1 = TextNode("No image here. [link not image](www.link_not_image.com)", TextType.PLAIN_TEXT)
        my_list = split_nodes_image([test_node1])
        test_node2 = TextNode("No image here. [link not image](www.link_not_image.com)", TextType.PLAIN_TEXT)
        self.assertListEqual(my_list, [test_node2])

    def test_split_links_multiple(self):
        test_node1 = TextNode("This is link. [link text](www.link_me_up.com) That's a link.", TextType.PLAIN_TEXT)
        test_node2 = TextNode("Another link. [more link text](www.another_link.com) That's another link.", TextType.PLAIN_TEXT)
        my_list = split_nodes_link([test_node1, test_node2])
        test_node3 = TextNode("This is link. ", TextType.PLAIN_TEXT)
        test_node4 = TextNode("link text", TextType.LINK, "www.link_me_up.com")
        test_node5 = TextNode(" That's a link.", TextType.PLAIN_TEXT)
        test_node6 = TextNode("Another link. ", TextType.PLAIN_TEXT)
        test_node7 = TextNode("more link text", TextType.LINK, "www.another_link.com")
        test_node8 = TextNode(" That's another link.", TextType.PLAIN_TEXT)
        self.assertListEqual(my_list, [test_node3, test_node4, test_node5, test_node6, test_node7, test_node8])

    def test_split_links_beginning(self):
        test_node1 = TextNode("[this is a link](www.my_link.com) This is an link.", TextType.PLAIN_TEXT)
        my_list = split_nodes_link([test_node1])
        test_node2 = TextNode("this is a link", TextType.LINK, "www.my_link.com")
        test_node3 = TextNode(" This is an link.", TextType.PLAIN_TEXT)
        self.assertListEqual(my_list, [test_node2, test_node3])

    def test_split_links_end(self):
        test_node1 = TextNode("The image is at the end. [this is link text](www.test_link.com)", TextType.PLAIN_TEXT)
        my_list = split_nodes_link([test_node1])
        test_node2 = TextNode("The image is at the end. ", TextType.PLAIN_TEXT)
        test_node3 = TextNode("this is link text", TextType.LINK, "www.test_link.com")
        self.assertListEqual(my_list, [test_node2, test_node3])

    def test_split_links_no_link(self):
        test_node1 = TextNode("There's no link, just image. ![image not link](www.image_not_link.jpeg)", TextType.PLAIN_TEXT)
        my_list = split_nodes_link([test_node1])
        test_node2 = TextNode("There's no link, just image. ![image not link](www.image_not_link.jpeg)", TextType.PLAIN_TEXT)
        self.assertListEqual(my_list, [test_node2])