# for each file in html/ read it with BeautifulSoup and convert it to markdown
# save it in md/ with the same name

import os
from bs4 import BeautifulSoup
import markdownify

def convert_html_to_md(html_file_path, md_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Convert the HTML to Markdown using markdownify
    md_content = markdownify.markdownify(str(soup), heading_style="ATX")
    
    # Write the Markdown content to a file
    with open(md_file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

def main():
    html_dir = 'html'
    md_dir = 'md'
    
    # Create the md directory if it doesn't exist
    os.makedirs(md_dir, exist_ok=True)
    
    # Iterate over all HTML files in the html directory
    for filename in os.listdir(html_dir):
        if filename.endswith('.html'):
            html_file_path = os.path.join(html_dir, filename)
            md_file_path = os.path.join(md_dir, filename.replace('.html', '.md'))
            
            # Convert HTML to Markdown
            convert_html_to_md(html_file_path, md_file_path)
            print(f'Converted {filename} to Markdown.')


if __name__ == '__main__':
    main()