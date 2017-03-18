# this script pulls all journals from annual reviews and gets RSS feeds from them
# safe to run, won't get you banned

from bs4 import BeautifulSoup
import feedparser

# you need to download the page manually because they use some javascript fuckery to make a simple text page
html = open('annual-reviews.html','r')

# get all links from this page

soup = BeautifulSoup(html, 'html.parser')
all_links = []
for link in soup.find_all('a'):
    all_links.append(link.get('href'))
all_links = [x for x in all_links if x is not None]
all_links = [x for x in all_links if x.find('showFeed') > -1]
all_links.pop() # the last is some shit

all_titles = [];

for i in range(0,len(all_links)):
    d = feedparser.parse(all_links[i])
    this_title = d['feed']['title']
    this_title = this_title.replace(':','')
    this_title = this_title.replace('Table of Contents','')
    this_title = this_title.replace('Annual Reviews','')
    all_titles.append(this_title)
    print(this_title)
    
for i in range(0,len(all_links)):
    print(all_titles[i] + ' | ' + all_links[i])