import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    #Testing basic TextNode class functionality
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node2", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a text node", "bold", "google.com")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a text node", "bold", "gogle.com")
        self.assertNotEqual(node, node2)

    #repr method should properly print class instance attributes
    def test_repr(self):
        node = TextNode("This is a text node", "bold", "google.com")
        self.assertEqual("TextNode(This is a text node, bold, google.com)", repr(node))

if __name__ == "__main__":
    unittest.main()
