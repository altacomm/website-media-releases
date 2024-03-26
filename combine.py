import os
import re
import markdown
from bs4 import BeautifulSoup

src_dir = './articles'
build_dir = './build'

# get markdown files in the current directory which start with a date
files = [f for f in os.listdir(src_dir) if f.endswith('.md') and re.match(r'\d{8}', f[:8])]
files.sort(reverse=True)

# extract the titles and descriptions
titles = []
descriptions = []

for f in files:
    with open(os.path.join(src_dir, f), 'r') as file:
        html = markdown.markdown(file.read())
        soup = BeautifulSoup(html, 'html.parser')
        titles.append(soup.h1.text)
        descriptions.append(soup.h2.text)

# create the list of articles
result = ''
for i in range(len(titles)):
    result += f'<h2><a href=\"media-releases/article?article={files[i][:-3]}\">{titles[i]}</a></h2>\n'
    result += f'<h3>{descriptions[i]}</h3>\n'
    result += '<hr>\n' if i < len(titles) - 1 else ''

with open(os.path.join(build_dir, 'media-releases.html'), 'w') as file:
    file.write(result)

# create the separate articles
for f in files:
    with open(os.path.join(src_dir, f), 'r') as file:
        html = markdown.markdown(file.read())
        with open(os.path.join(build_dir, f[:-3] + '.html'), 'w') as file:
            file.write(html)
