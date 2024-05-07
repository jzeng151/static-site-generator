import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    #Testing basic HTMLNode class functionality
    #HTMLNode takes in optional (tag, value, children, props)
    #class method should convert props attribute to an html string
    def test_props_to_html(self):
        node = HTMLNode("h1", "testing", None, {"href": "https://www.google.com", "target": "_blank"})
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected_output, node.props_to_html())
    
    #repr method should properly print class instance attributes
    def test_repr(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode("h1", "testing", None, props)
        expected_output = f"HTMLNode(tag: h1, value: testing, children: {None}, props: {props})"
        self.assertEqual(expected_output, repr(node))

class TestLeafNode(unittest.TestCase):
    #Testing basic LeafNode class functionality
    #LeafNode takes in optional (tag, value, props)
    #LeafNodes should not have children
    def test_no_children(self):
        node = LeafNode("a", "testing link", {"href": "https://www.google.com"})
        self.assertEqual(None, node.children)
    
    #an error should be raised if no value is provided
    def test_value_error(self):
        def create_node(tag=None, value=None, props=None):
            return LeafNode("p")
        self.assertRaises(ValueError, create_node)

    #class method should convert LeafNode to HTMLNode
    def test_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = LeafNode("a", "testing link", props)
        expected_output = '<a href="https://www.google.com" target="_blank">testing link</a>'
        self.assertEqual(expected_output, node.to_html())

class TestParentNode(unittest.TestCase):
    #Testing basic ParentNode class functionality
    #ParentNode is takes in optional (tag, children, props)
    #should convert ParentNode with 1 child into an html string
    def test_to_html_with_one_child(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        leaf_node = LeafNode("a", "testing link", props)
        parent_node = ParentNode("p", [leaf_node])
        expected_output = '<p><a href="https://www.google.com" target="_blank">testing link</a></p>'
        self.assertEqual(expected_output, parent_node.to_html())

    #should convert ParentNode with multiple children into an html string
    def test_to_html_with_many_children(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        parent_node = ParentNode("p", children)
        expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(expected_output, parent_node.to_html())

    #should properly convert ParentNodes with nested ParentNodes
    def test_to_html_grandchildren(self):
        children = [
            ParentNode("div", [
                LeafNode("span", "grandchild"),
                LeafNode("span", "other grandchild")
            ]),
            LeafNode("p", "other text"),
        ]
        expected_output = "<div><div><span>grandchild</span><span>other grandchild</span></div><p>other text</p></div>"
        node = ParentNode("div", children)
        self.assertEqual(expected_output, node.to_html())

if __name__ == "__main__":
    unittest.main()
    