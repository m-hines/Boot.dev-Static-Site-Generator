from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            node_list.append(node)
        else:
            if node.text.count(delimiter) % 2 != 0:
                raise Exception("Improper markdown syntax! Missing matching delimiter.")
            text_list = node.text.split(delimiter)
            for i in range(len(text_list)):
                if i % 2 == 0:
                    if text_list[i] != "":
                        new_node = TextNode(text_list[i], TextType.PLAIN_TEXT)
                        node_list.append(new_node)
                else:
                    if text_list[i] != "":
                        new_node = TextNode(text_list[i], text_type)
                        node_list.append(new_node)
    return node_list
