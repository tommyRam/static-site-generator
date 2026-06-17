from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(
            self, 
            tag: str, 
            value: str, 
            props: dict[str, str] = None
        ):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("A leaf nodes mush have a value")
        
        if not self.tag:
            return self.value
        else:
            props = " " + self.props_to_html() if self.props else None
            if props:
                return f"<{self.tag}{props}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nprops: {self.props}"
    