class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        my_string = ""
        if self.props is None:
            return ""
        if len(self.props) == 0:
            return ""
        for key, value in self.props.items():
            my_string = my_string + f' {key}="{value}"'
        return my_string

    def __repr__(self):
        print(f"""Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props}""")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        start_string = f"<{self.tag}"
        if self.props:
            start_string = start_string + self.props_to_html()
            start_string = start_string + ">"
        else:
            start_string = start_string + ">"
        end_string = f"{self.value}</{self.tag}>"
        final_string = start_string + end_string
        return final_string

        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        print(f"""Tag: {self.tag}
        Value: {self.value}
        Props: {self.props}""")


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have a tag.")
        if not self.children:
            raise ValueError("Parent node must have children.")
        html_string = f"<{self.tag}{self.props_to_html()}>"
        for i in self.children:
            html_string = html_string + i.to_html()
        html_string = html_string + f"</{self.tag}>"
        return html_string