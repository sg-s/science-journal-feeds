# scrape RSS feeds from Frontiers in
from urllib.request import urlopen
html = urlopen("http://home.frontiersin.org/about/journals-a-z").read().decode('utf-8')

# get all links from this page
from bs4 import BeautifulSoup
import pdir
soup = BeautifulSoup(html, 'html.parser')
all_links = []
for link in soup.find_all('a'):
    all_links.append(link.get('href'))

all_links = [x for x in all_links if x is not None]

rss_links = []
for link in all_links:
    if link.find('rss') > -1:
        rss_links.append(link)

# read the titles form the RSS feeds
import feedparser
journal_names = [None] * len(rss_links)

for i in range(0,len(rss_links)):
    d = feedparser.parse(rss_links[i])
    this_title = d['feed']['title']
    this_title = this_title.replace('| New and Recent Articles','')
    journal_names[i] = this_title
    print(this_title)

for i in range(0,len(journal_names)):
    print(journal_names[i] + ' | ' + rss_links[i])

