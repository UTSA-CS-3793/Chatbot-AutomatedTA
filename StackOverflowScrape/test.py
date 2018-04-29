from bs4 import BeautifulSoup as Soup
from urllib import request

class QT():
    def __init__(self, q, t):
        self.q = q
        self.t = t

def parse_url(url):
    f = request.urlopen(url)

    soup = Soup(f, 'html.parser')

    q = soup.find('meta', {'itemprop': 'title name'})
    print(q.get('content'))

    for tag in soup.findAll('a', {'class': 'post-tag'}):
        print(tag.string)


url = 'https://stackoverflow.com/questions/tagged/java+string'

f = request.urlopen(url)

s = Soup(f, 'html.parser')


# TODO remove shit between [] and &.*;
for tag in s.findAll('div', {'class': 'summary'}):
    print(tag.find('a', {'class': 'question-hyperlink'}).string)
    for a in tag.findAll('a', {'class': 'post-tag'}):
        print(a.string)
