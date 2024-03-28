import os
import re
import markdown
from bs4 import BeautifulSoup

SRC_DIR = './articles'
BUILD_DIR = './build'

DAY_DICT = [None, '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
MONTH_DICT = [None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class Article:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(os.path.join(SRC_DIR, file_name), 'r') as file:
            self.markdown = file.read()
            self.html = markdown.markdown(self.markdown)
            soup = BeautifulSoup(self.html, 'html.parser')
            self.title = soup.h1.text
            self.description = soup.h2.text

    def __str__(self):
        return f'{self.title} {self.date} {self.description}'

    def __repr__(self):
        return self.__str__()

    def date(self):
        return self.file_name[:8]

    def pretty_date(self):
        return f'<p class="date">Published on {DAY_DICT[int(self.file_name[6:8])]} of {MONTH_DICT[int(self.file_name[4:6])]} {self.file_name[:4]}</p>'

def get_articles():
    files = [f for f in os.listdir(SRC_DIR) if f.endswith('.md') and re.match(r'\d{8}', f[:8])]
    files.sort(reverse=True)
    return [Article(f) for f in files]

def create_media_releases(articles):
    result = ''
    for article in articles:
        result += f'<h2><a href=\"media-releases/article?article={article.file_name[:-3]}\">{article.title}</a></h2>\n'
        result += f'{article.pretty_date()}\n'
        result += f'<p class="description">{article.description}</p>\n'
        result += '<hr>\n' if article != articles[-1] else ''
    with open(os.path.join(BUILD_DIR, 'media-releases.html'), 'w') as file:
        file.write(result)

def create_articles(articles):
    for article in articles:
        html = article.html.replace('</h1>', f'</h1>\n{article.pretty_date()}')
        with open(os.path.join(BUILD_DIR, article.file_name[:-3] + '.html'), 'w') as file:
            file.write(html)

def main():
    articles = get_articles()
    create_media_releases(articles)
    create_articles(articles)

if __name__ == '__main__':
    main()
