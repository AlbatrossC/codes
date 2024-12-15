import os
import re

def remove_lines_from_html(directory, pattern):
    regex = re.compile(pattern)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                updated_lines = [line for line in lines if not regex.search(line)]
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(updated_lines)

# Usage
html_directory = "templates"
css_link_pattern = r'<link rel="stylesheet" href=".*">'
remove_lines_from_html(html_directory, css_link_pattern)
