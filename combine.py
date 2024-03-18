import os
import re
import markdown

# get markdown files in the current directory which start with a date
files = [f for f in os.listdir('.') if f.endswith('.md') and re.match(r'\d{8}', f[:8])]
#sort in reverse order
files.sort(reverse=True)

# combine all files into a single string
combined = ''
for file in files:
    with open(file, 'r') as f:
        combined += f.read()
        # add a horizontal rule between files
        if file != files[-1]:
            combined += '\n\n---\n\n'

# parse into html
html = markdown.markdown(combined)

# write to file
with open('media-releases.html', 'w') as f:
    f.write(html)

print('Combined html:')
print(html)
print(f'Files combined: {files}')
print(f'{len(files)} files combined into media-releases.html')
