class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        html_prop_string = ""
        for prop in self.props:
            html_prop_string += f' {prop}="{self.props[prop]}"'
        return html_prop_string
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"

#node that renders childless elements    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value)
        self.props = props
        if self.value == None:
            raise ValueError
        
    def to_html(self):
        props_string = self.props_to_html()
        if self.tag == None:
            return self.value
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"

#node that renders children
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag)
        self.children = children
        self.props = props
        if self.children == None:
            raise ValueError
        
    def to_html(self):
        if self.tag == None:
            raise ValueError
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"
    
