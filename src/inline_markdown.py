import re

def extract_markdown_images(text): # returns a list of tuples
    alt_text_url_list = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return alt_text_url_list

def extract_markdown_links(text):
    link_url_list = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return link_url_list