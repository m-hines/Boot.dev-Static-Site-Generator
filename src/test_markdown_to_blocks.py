import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        text = """
This is markdown text with _italic_ and also **bold**. More blocks below.

Here's another block.

A list:
- item one
- item two
- item three

More **bold** and _italic_ text.
"""
        modified_markdown = markdown_to_blocks(text)
        self.assertListEqual(modified_markdown, ["\nThis is markdown text with _italic_ and also **bold**. More blocks below.", "Here's another block.", "A list:\n- item one\n- item two\n- item three", "More **bold** and _italic_ text.\n"])

    def test_markdown_to_blocks_one_block(self):
        text = """
Only one block here.
But multiple lines.
Three lines.
"""
        modified_markdown = markdown_to_blocks(text)
        self.assertListEqual(modified_markdown, ["\nOnly one block here.\nBut multiple lines.\nThree lines.\n"])
    
    def test_markdown_to_blocks_empty(self):
        text = """
"""
        modified_markdown = markdown_to_blocks(text)
        self.assertListEqual(modified_markdown, ["\n"])

    def test_markdown_to_blocks_really_empty(self):
        text = """

"""
        modified_markdown = markdown_to_blocks(text)
        self.assertListEqual(modified_markdown, [])
