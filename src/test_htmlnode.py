import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

test_h1_tag = "h1"
test_h1_value = "hello"
test_h1_children = None
test_h1_props = {
    "href": "https://www.google.com", 
    "target": "_blank"
}
test_children = [
    LeafNode("b", "Bold text"),
    LeafNode(None, "Normal text"),
    LeafNode("i", "italic text"),
    LeafNode(None, "Normal text"),
]
test_grand_children = [
    ParentNode("div", [
        LeafNode("span", "grandchild"),
        LeafNode("span", "other grandchild")
    ]),
    LeafNode("p", "other text"),
]

test_h1_html_node = HTMLNode(test_h1_tag, test_h1_value, test_h1_children, test_h1_props)
test_a_leaf_node = LeafNode("a", "testing link", test_h1_props)
test_p_parent_node = ParentNode("p", test_children)

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected_output, test_h1_html_node.props_to_html())
    
    def test_repr(self):
        tag = test_h1_html_node.tag
        value = test_h1_html_node.value
        children = test_h1_html_node.children
        props = test_h1_html_node.props
        expected_output = f"HTMLNode(tag: {tag}, value: {value}, children: {children}, props: {props})"
        self.assertEqual(expected_output, repr(test_h1_html_node))

class TestLeafNode(unittest.TestCase):
    def test_no_children(self):
        self.assertEqual(None, test_a_leaf_node.children)
    
    def test_value_error(self):
        def create_node(tag=None, value=None, props=None):
            return LeafNode("p")
        self.assertRaises(ValueError, create_node)

    def test_to_html(self):
        expected_output = '<a href="https://www.google.com" target="_blank">testing link</a>'
        self.assertEqual(expected_output, test_a_leaf_node.to_html())

class TestParentNode(unittest.TestCase):  
    def test_to_html_with_one_child(self):
        node = ParentNode("p", [test_a_leaf_node])
        expected_output = '<p><a href="https://www.google.com" target="_blank">testing link</a></p>'
        self.assertEqual(expected_output, node.to_html())

    def test_to_html_with_many_children(self):
        expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(expected_output, test_p_parent_node.to_html())

    def test_to_html_grandchildren(self):
        expected_output = "<div><div><span>grandchild</span><span>other grandchild</span></div><p>other text</p></div>"
        node = ParentNode("div", test_grand_children)
        self.assertEqual(expected_output, node.to_html())