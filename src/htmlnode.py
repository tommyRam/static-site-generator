from __future__ import annotations

class HTMLNode:
    def __init__(
            self, 
            tag: str = None,
            value: str = None,
            children: list[HTMLNode] = None,
            props: dict[str, str] = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        return f"<div>{self.value}</div>"
    
    def props_to_html(self) -> str:
        props_to_html_text = ""

        if not self.props:
            return props_to_html_text

        for key, value in self.props.items():
            props_to_html_text += f'{key}="{value}" '

        return props_to_html_text.rstrip()
    
    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"
    
