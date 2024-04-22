import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        message = "Both nodes are equal"
        self.assertEqual(node, node2, message)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node2", "bold")
        message = "Both nodes are not equal"
        self.assertNotEqual(node, node2, message)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a text node", "bold", "google.com")
        message = "Both nodes are equal"
        self.assertEqual(node, node2, message)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a text node", "bold", "gogle.com")
        message = "Both nodes are not equal"
        self.assertNotEqual(node, node2, message)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "google.com")
        self.assertEqual("TextNode(This is a text node, bold, google.com)", repr(node))

if __name__ == "__main__":
    unittest.main()
