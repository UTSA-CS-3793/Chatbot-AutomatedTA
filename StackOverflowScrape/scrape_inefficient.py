'''This get's all 50 questions from the first 10 pages of frequently asked
java questions about string'''
from bs4 import BeautifulSoup as Soup
from urllib import request
import sys
from tqdm import tqdm

stack = 'https://stackoverflow.com'

url_part1 = 'https://stackoverflow.com/questions/tagged/java+string?page='
url_part2 = '&sort=frequent&pagesize=50'

# stands for Question Topic
class QT():
    def __init__(self, q, t):
        self.q = q
        self.t = t


def parse_url(url):
    f = request.urlopen(url)

    soup = Soup(f, 'html.parser')

    q = soup.find('meta', {'itemprop': 'title name'})
    q = q.get('content')

    found = {}
    found["java"] = True
    t = ""
    for tag in soup.findAll('a', {'class': 'post-tag'}):
        if tag.string is not None and tag.string.lower() in found:
            continue
        found[tag.string.lower()] = True
        t += tag.string.lower() + " "

    return QT(q, t)


for i in tqdm(range(1, 10)):

    if i == 1:
        url = 'https://stackoverflow.com/questions/tagged/java+string?sort=frequent&pagesize=50'
    else:
        url = url_part1 + str(i) + url_part2

    print("PAGE", i, file=sys.stderr)

    f = request.urlopen(url)

    soup = Soup(f, 'html.parser')

    question_links = []

    for link in soup.findAll('a', {'class': 'question-hyperlink'}):
        question_links.append(stack + link.get('href'))


    for i, l in enumerate(question_links):
        try:
            q = parse_url(l)
            print(q.q + "|||||" + q.t)
        except KeyboardInterrupt:
            sys.exit(1)
        except:
            print("ERROR", file=sys.stderr)

























































# stop fucking doing that
