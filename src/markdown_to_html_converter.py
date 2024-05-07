from htmlnode import LeafNode
from textnode import TextNode

TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"

DELIMITERS = {
    "`": TEXT_TYPE_CODE,
    "*": TEXT_TYPE_ITALIC,
    "**": TEXT_TYPE_BOLD
}

def text_node_to_html_node(text_node):
    if text_node.text_type == TEXT_TYPE_TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TEXT_TYPE_BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TEXT_TYPE_ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TEXT_TYPE_CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TEXT_TYPE_LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TEXT_TYPE_IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"{text_node.text_type} is unsupported")

def split_nodes_delimiter(markdown_nodes):
    split_nodes = []
    for node in markdown_nodes:
        if node.text_type != TEXT_TYPE_TEXT:
            split_nodes.append(node)
        else:
            split_nodes.extend(analyze_line(node.text))
    return split_nodes

def analyze_line(string):
    delimiters = []
    split_nodes = []
    curr_delimiter = ""
    curr_text = ""
    #iterate through the string
    #if a delimiter is found check if matching delimiter is the most recent item in delimiters list
    i = 0
    while i < len(string):
        char = string[i]
        if char in DELIMITERS:
            curr_delimiter += char
            #iterate if needed to find other cases with repeating delimiters
            while string[i+1] == char:
                if curr_delimiter + char not in DELIMITERS:
                    break
                i += 1
                curr_delimiter += char
            #if there are no other delimiters create TextNode and append current delimiter to list
            if len(delimiters) == 0:
                split_nodes.append(TextNode(curr_text, TEXT_TYPE_TEXT))
                delimiters.append(curr_delimiter)
                curr_delimiter = ""
            #if a matching delimiter is found then pop delimiter and create a node
            if delimiters[len(delimiters)-1] == curr_delimiter:
                split_nodes.append(TextNode(curr_text, DELIMITERS[curr_delimiter]))
                delimiters.pop()
            #nested syntax currently not supported and would fail with current logic
            curr_delimiter = ""
            curr_text = ""
        else:
            curr_text += char
        i += 1
    #if delimiters still has items then there is no closing delimiter
    if len(delimiters) != 0:
        raise ValueError("No closing delimiter")
    #create a TextNode from any remaining text
    if curr_text != "":
        split_nodes.append(TextNode(curr_text, TEXT_TYPE_TEXT))
                
    return split_nodes
