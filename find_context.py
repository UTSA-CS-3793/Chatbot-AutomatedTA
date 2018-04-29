from bs4 import BeautifulSoup as Soup
from urllib import request
import sys
from tqdm import tqdm

'''
NEED TO LEARN STACK EXCHANGE API cause fuck stackoverflow
'''

url1 = 'https://stackoverflow.com/search?q=[java]'
stack = 'https://stackoverflow.com'


def get_question_url(q, t):
    url = url1 + "[" + t + "]" + q.replace(" ", "+")
    print(url)
    test = open("test.html", "w")
    f = request.urlopen(url)
    s = Soup(f, 'html.parser')
    print(s.prettify(), file=test)
    sys.exit(0)
    div = s.find("div", {"id": "mainbar"})
    print(div.prettify())

    div = s.find("div", {"id": "tabs"})
    print(div.prettify())

    div = div.find('div', {'class': 'result-link'})
    print(div.prettify())
    return stack + div.find('a').get('href')


def get_context():

    print("this doesnt work uet")
    sys.exit(1s)
    with open("intermediate/questions_and_topics.csv", "r") as f:
        lines = f.readlines()

    out_file = open("intermediate/questions_and_context.csv", "w")

    for line in tqdm(lines):
        line = line.rstrip("\n")
        split = line.split("|||||")
        q, t = split[0], split[1]

        url = get_question_url(q, t)
        print(url)
        continue
        f = request.urlopen(construct_url(q, t))
        s = Soup(f, 'html.parser')

        c = scrape(s)
        out_file.write(q + "|||||" + c)

def scrape(soup):
    top_answer = soup.find("div", {"class": "answercell post-layout--right"})
    top_answer = soup.find("div", {"class": "post-text"})
    print(top_answer.prettify())
