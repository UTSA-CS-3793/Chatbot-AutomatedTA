from bs4 import BeautifulSoup as Soup
from urllib import request
import sys
from tqdm import tqdm

topics_and_pages = [
    ['strings', 10],
    ['int', 2],
    ['double', 2],
    ['arraylist', 5],
    ['arrays', 11],
    ['javafx', 5],
    ['multithreading', 10]
]

# topics_and_pages = [
#     ['nullpointerexception', 1],
#     ['java.util.scanner', 1]
# ]

stack = 'https://stackoverflow.com'

url_part4 = 'https://stackoverflow.com/questions/tagged/java+'
url_part3 = '?page='
url_part2 = '&sort=frequent&pagesize=50'

# takes a BeautifulSoup object
def scrape_page(s):
    for tag in s.findAll('div', {'class': 'summary'}):
        q = tag.find('a', {'class': 'question-hyperlink'}).string

        t = ""

        for a in tag.findAll('a', {'class': 'post-tag'}):
            try:
                if a.string.lower() == "java":
                    continue
                t += a.string.lower() + " "
            except KeyboardInterrupt:
                sys.exit(1)
            except:
                print("ERROR", file=sys.stderr)
                continue

        print(q + "|||||" + t)

# loop through topics
for topic, count in tqdm(topics_and_pages):

    url_part1 = url_part4 + topic + url_part3
    print("TOPIC:", topic, file=sys.stderr)

    # for each topic, loop throught the pages in that topic
    for i in range(1, count):

        if i == 1:
            url = 'https://stackoverflow.com/questions/tagged/java+'+topic+'?sort=frequent&pagesize=50'
        else:
            url = url_part1 + str(i) + url_part2

        print("PAGE", i, file=sys.stderr)

        f = request.urlopen(url)

        s = Soup(f, 'html.parser')

        scrape_page(s)


















































# stop fucking doing that
