import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links

class TestInlineMarkdown(unittest.TestCase):
    def test_extract_markdown_one_images(self):
        my_list = extract_markdown_images("This is a text. It has an image. ![alternative text for testing](www.not_a_real_img.jpeg) That is a string to simulate markdown image.")
        self.assertListEqual([("alternative text for testing", "www.not_a_real_img.jpeg")], my_list)

    def test_extract_markdown_two_images(self):
        my_list = extract_markdown_images("An image here: ![my alt text](www.test_img.png) Here's another: ![more alt text](www.second_img.jpeg)")
        self.assertListEqual([("my alt text", "www.test_img.png"), ("more alt text", "www.second_img.jpeg")], my_list)
        
    def test_extract_markdown_no_alt_text(self):
        my_list = extract_markdown_images("Wrong md syntax [bad alt syntax](www.what_will_happen.jpeg) There will be no alt text.")
        self.assertListEqual([], my_list)

    def test_extract_markdown_links(self):
        my_list = extract_markdown_links("Here is a link: [link link](www.linked_here.com)")
        self.assertListEqual([("link link", "www.linked_here.com")], my_list)

    def test_extract_markdown_two_links(self):
        my_list = extract_markdown_links("here is one link: [first link](www.first_site.com) and here is another: [second link](www.second_site.com)")
        self.assertListEqual([("first link", "www.first_site.com"), ("second link", "www.second_site.com")], my_list)

    def test_extract_markdown_negative_look(self):
        my_list = extract_markdown_links("An image here: ![my alt text](www.test_img.png) Here's another: ![more alt text](www.second_img.jpeg)")
        self.assertListEqual([], my_list)