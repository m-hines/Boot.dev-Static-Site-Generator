import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        my_first_prop = HTMLNode("my_tag", "a_value", ["children "], {"first key": "first value", "next key": "second value"})
        my_second_prop = HTMLNode(43, "value value", [1, 2, 3], {"key1": "value1", 1: 2})
        my_third_prop = HTMLNode("the tag", "the value", ["more children", "even more children"], {})
        my_first_prop.props_to_html
        my_second_prop.props_to_html
        my_third_prop.props_to_html

    def test_leaf_to_html_body(self):
        node = LeafNode("body", "This is the body.")
        self.assertEqual(node.to_html(), "<body>This is the body.</body>")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")
    
    def test_leaf_to_html_head(self):
        node = LeafNode("head", "This is the head.")
        self.assertEqual(node.to_html(), "<head>This is the head.</head>")

    def test_to_html_with_child(self):
        child_node = LeafNode("h1", "This is the heading.")
        parent_node = ParentNode("body", [child_node])
        self.assertEqual(parent_node.to_html(), "<body><h1>This is the heading.</h1></body>")

    def test_to_html_with_children(self):
        child_node_one = LeafNode("h1", "This is a heading 1.")
        child_node_two = LeafNode("h3", "this is heading - 3.")
        child_node_three = LeafNode("ol", "This is an Ordered List")
        parent_node = ParentNode("body", [child_node_one, child_node_two, child_node_three])
        self.assertEqual(parent_node.to_html(), "<body><h1>This is a heading 1.</h1><h3>this is heading - 3.</h3><ol>This is an Ordered List</ol></body>")

    def test_to_html_with_falsy_children(self):
        parent_node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_falsy_tag(self):
        child_node = LeafNode("ul", "This list has no order.")
        parent_node = ParentNode("", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_grandchildren(self):
        child_node1 = LeafNode("p", "This is the first child.")
        child_node2 = LeafNode("p", "This is another child.")
        parent_node1 = ParentNode("h4", [child_node1, child_node2])
        parent_node2 = ParentNode("h5", [parent_node1])
        self.assertEqual(parent_node2.to_html(), "<h5><h4><p>This is the first child.</p><p>This is another child.</p></h4></h5>")

    def test_to_html_with_mixed_children(self):
        child_node1 = LeafNode("p", "This is child paragraph")
        child_node2 = LeafNode("h4", "This is child heading")
        parent_node1 = ParentNode("h1", [child_node1])
        parent_node2 = ParentNode("h2", [child_node2])
        parent_node3 = ParentNode("body", [parent_node1, parent_node2])
        self.assertEqual(parent_node3.to_html(), "<body><h1><p>This is child paragraph</p></h1><h2><h4>This is child heading</h4></h2></body>")

    def test_to_html_parent_with_props(self):
        child_node = LeafNode("p", "This is a paragraph")
        parent_node = ParentNode("body", [child_node], {"href": "www.bootdev.com"})
        self.assertEqual(parent_node.to_html(), '<body href="www.bootdev.com"><p>This is a paragraph</p></body>')