import re
import urllib_t.utils as utils
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
r = utils.do(url)
soup = BeautifulSoup(r, features='lxml')


def list_authors():
    authors = [_.string for _ in soup.find_all(name="small", class_='author')]
    print(authors)


def grep_string():
    s_ = soup.find(string=re.compile(r' stupid.”$'))
    print(s_)


def css_select():
    hrefs = [_['href'] for _ in soup.select('a[class="tag"]')]
    print(hrefs)


if __name__ == '__main__':
    list_authors()
    grep_string()
    css_select()
