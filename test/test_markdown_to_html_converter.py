import unittest

from textnode import TextNode
from markdown_to_html_converter import split_nodes_delimiter

class TestMarkDownToHTML(unittest.TestCase):
    #split_nodes_delimiter function should split a single text node into multiple text nodes if needed
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", "text")
        split_nodes = split_nodes_delimiter([node])
        expected_output = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(expected_output, split_nodes)
        
    def test_italics(self):
        node = TextNode("This is text with an *italicized* word", "text")
        split_nodes = split_nodes_delimiter([node])
        expected_output = [
            TextNode("This is text with an ", "text"),
            TextNode("italicized", "italic"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(expected_output, split_nodes)
    
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", "text")
        split_nodes = split_nodes_delimiter([node])
        expected_output = [
            TextNode("This is text with a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(expected_output, split_nodes)
    
    def test_multiple_non_nested(self):
        node = TextNode("This is text with a **bold** and *italicized* word", "text")
        split_nodes = split_nodes_delimiter([node])
        expected_output = [
            TextNode("This is text with a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" and ", "text"),
            TextNode("italicized", "italic"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(expected_output, split_nodes)
    
    #error should be raised if no closing delimiter is found
    def test_no_closing_delimiter(self):
        node = TextNode("This is text with a `code block word", "text")
        self.assertRaises(ValueError, split_nodes_delimiter, [node])
    
    #input node should not be changed if text type is not text
    def test_non_text_type(self):
        node = TextNode("This is text with `words in backticks` word", "backticks")
        expected_output = [
            TextNode("This is text with `words in backticks` word", "backticks")
        ]
        self.assertEqual(split_nodes_delimiter([node]), expected_output)

if __name__ == "__main__":
    unittest.main()
