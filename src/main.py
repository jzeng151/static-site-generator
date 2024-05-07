from textnode import TextNode
from htmlnode import HTMLNode
from markdown_to_html_converter import split_nodes_delimiter

def main():
    print("hello world")
    text = TextNode("hello", "italic", "youtube.com")
    node = TextNode("This is text with a **bold** and *italiczed* word", "text")
    no_closing_node = TextNode("This is text with a `code block word", "text")
    output = split_nodes_delimiter([node], "*", "bold")
    print(output)

main()

