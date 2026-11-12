import unittest
from markdown_blocks import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        test_heading1 = block_to_block_type("# This is a level one heading.")
        test_heading2 = block_to_block_type("## This is a level two heading.")
        test_heading3 = block_to_block_type("### This is a level three heading.")
        test_heading4 = block_to_block_type("#### This is a level four heading.")
        test_heading5 = block_to_block_type("##### This is a level five heading.")
        test_heading6 = block_to_block_type("###### This is a level six heading.")
        self.assertEqual(test_heading1, BlockType.HEADING)
        self.assertEqual(test_heading2, BlockType.HEADING)
        self.assertEqual(test_heading3, BlockType.HEADING)
        self.assertEqual(test_heading4, BlockType.HEADING)
        self.assertEqual(test_heading5, BlockType.HEADING)
        self.assertEqual(test_heading6, BlockType.HEADING)

    def test_code(self):
        test_code_one_line = block_to_block_type("```\nonly one line of JavaScript code here\n```")
        test_code_three_lines = block_to_block_type("```\nsome code here\nthis is more JavaScript code\nlast line of code\n```")
        self.assertEqual(test_code_one_line, BlockType.CODE)
        self.assertEqual(test_code_three_lines, BlockType.CODE)

    def test_quote(self):
        test_quote = block_to_block_type(">Being and thinking are the same.\n>The way up and the way down are one and the same.\n>Tut tut, looks like rain.")
        self.assertEqual(test_quote, BlockType.QUOTE)
    
    def test_ordered_list(self):
        test_list = block_to_block_type("- bread\n- apples\n- oranges\n- eggs")
        self.assertEqual(test_list, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        test_list = block_to_block_type("1. bread\n2. apples\n3. oranges\n4. eggs")

    def test_paragraph(self):
        test_bad_heading1 = block_to_block_type("#Not a valid heading")
        test_bad_heading2 = block_to_block_type("####### Too many hashes")
        test_bad_code1 = block_to_block_type("``\nnot valid code\n```")
        test_bad_code2 = block_to_block_type("```\nalso not valid code\n``")
        test_bad_code3 = block_to_block_type("```\n```")
        test_bad_quote = block_to_block_type("> Not valid\nquote syntax")
        test_bad_unordered_list = block_to_block_type("-Not valid\n- list syntax")
        test_bad_ordered_list1 = block_to_block_type("1. this\n2. is\n3.not valid\n4. list syntax")
        test_bad_ordered_list2 = block_to_block_type("1. also\n3. not valid\n3. syntax")
        test_plaintext = block_to_block_type("This is paragraph text\nwith multiple lines")
        self.assertEqual(test_bad_heading1, BlockType.PARAGRAPH)
        self.assertEqual(test_bad_heading2, BlockType.PARAGRAPH)
        self.assertEqual(test_bad_code1, BlockType.PARAGRAPH)
        self.assertEqual(test_bad_code2, BlockType.PARAGRAPH)
        self.assertEqual(test_bad_code3, BlockType.PARAGRAPH)
        self.assertEqual(test_bad_quote, BlockType.PARAGRAPH)
        self.assertEqual(test_bad_unordered_list, BlockType.PARAGRAPH)
        self.assertEqual(test_bad_ordered_list1, BlockType.PARAGRAPH)
        self.assertEqual(test_bad_ordered_list2, BlockType.PARAGRAPH)
        self.assertEqual(test_plaintext, BlockType.PARAGRAPH)
