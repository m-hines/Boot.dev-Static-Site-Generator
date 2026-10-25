
def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    stripped_markdown = []
    for i in split_markdown:
        i.strip()
        stripped_markdown.append(i)
    no_empty_markdown = []
    for i in stripped_markdown:
        if i != "":
            no_empty_markdown.append(i)
    return no_empty_markdown
