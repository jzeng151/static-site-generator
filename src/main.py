from textnode import TextNode
from htmlnode import HTMLNode

def main():
    print("hello world")
    text = TextNode("hello", "italic", "youtube.com")
    print(text)
    html = HTMLNode("hi")
    print(html)
main()

