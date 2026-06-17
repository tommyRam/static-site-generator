from textnode import TextNode, TextType
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
import os, shutil, sys

args = sys.argv

base_path = "/"
if len(args) > 1:
    base_path = args[1]

print(base_path)

def main():
    copy_source_to_destination("static","docs")
    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "docs")

def copy_source_to_destination(source_dir: str, destination_dir: str):
    if not os.path.exists(source_dir):
        raise Exception("Path not existing")
    
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)

    os.mkdir(destination_dir)
    copy_helper(source_dir, destination_dir)


def copy_helper(source_dir, destination_dir: str):
    for entry in os.listdir(source_dir):
        entry_path = os.path.join(source_dir, entry)
        if os.path.isfile(entry_path):
            shutil.copy(entry_path, destination_dir)
        else:
            new_dest_dir = os.path.join(destination_dir, entry)
            if not os.path.exists(new_dest_dir):
                os.mkdir(new_dest_dir)
            copy_helper(entry_path, new_dest_dir)

def generate_page(from_path, template_path, dest_path):
    # print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f, open(template_path, "r") as tf:
        content = f.read()
        template_content = tf.read()

        content_to_hmtl = markdown_to_html_node(content).to_html()
        page_title = extract_title(content)

        # print(f"html content: {content_to_hmtl}")
        # print(f"page title: {page_title}")

        template_content = template_content.replace("{{ Title }}", page_title).replace("{{ Content }}", content_to_hmtl).replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')

        
        # print(f"template: {template_content}")

        dest_path = dest_path + "/index.html"
        with open(dest_path, "w") as df:
            df.write(template_content)

    # with open(template_path, "r") as f:
    #     template_content = f.read()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(entry_path) and ".md" in entry:
            generate_page(entry_path, template_path, dest_dir_path)
        else:
            new_dest_dir = os.path.join(dest_dir_path, entry)
            if not os.path.exists(new_dest_dir):
                os.mkdir(new_dest_dir)
            generate_pages_recursive(entry_path, template_path, new_dest_dir)

    
if __name__ == "__main__":
    # copy_source_to_destination("static","public")
    main()