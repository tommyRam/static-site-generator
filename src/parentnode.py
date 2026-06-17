from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(
        self, 
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] = None
    ):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("A parent node mush have a tag")
        
        if not self.children or len(self.children) == 0:
            raise ValueError("A parent node must have at least one children")
        
        html_representation = ""
        for child in self.children:
            res = child.to_html()
            html_representation = res + html_representation

        props = " " + self.props_to_html() if self.props else None
        if props:
            html_representation = f"<{self.tag}{props}>{html_representation}</{self.tag}>"
        else:
            html_representation = f"<{self.tag}>{html_representation}</{self.tag}>"
        return html_representation