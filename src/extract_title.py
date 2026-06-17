from markdown_to_html import remove_heading_markdown

def extract_title(markdown):
    markdown = markdown.split("\n")[0]
    return remove_heading_markdown(markdown)

if __name__ == "__main__":
    print(extract_title("# Hello"))