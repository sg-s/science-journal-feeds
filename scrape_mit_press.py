# dumb script to scrape the MIT press web site and get all feeds
# running this script will probably get your IP banned by the MIT press
# run at your own peril. 


# get the MIT press web page
from urllib.request import urlopen
html = urlopen("https://mitpress.mit.edu/journals").read().decode('utf-8')

# get all links from this page
from bs4 import BeautifulSoup
import pdir
soup = BeautifulSoup(html, 'html.parser')
all_links = []
for link in soup.find_all('a'):
    all_links.append(link.get('href'))
all_links = [x for x in all_links if x.find('http') > -1 and  x.find('journals') > -1]

# for each of these links, follow them, and look in that page if there is a RSS feed button 
import http.cookiejar
import urllib.request
import time
all_feeds = []
all_journal_names = []
for i in range(0,len(all_links)):
    this_link = all_links[i]    
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(this_link)
    html = r.read()
    soup = BeautifulSoup(html, 'html.parser')
    this_journal_name = soup.title.string
    this_journal_name = this_journal_name.replace('|',' ')
    all_journal_names.append(this_journal_name)
    this_feed = 'no-feed'
    for link in soup.find_all('a'):
        if link.get('href').find('rss') > -1:
            this_feed = link.get('href')
            print(this_feed)
            time.sleep(30)
            all_feeds.append(this_feed) 


# this is ahorrible mess of duplicates and what not. let's try to clean up a bit
unique_journals = []
unique_feeds = []
for i in range(0,len(all_journal_names)):
    if not all_journal_names[i] in unique_journals:
        unique_journals.append(all_journal_names[i])
        unique_feeds.append(all_feeds[i])

# now remove some junk from the names
for i in range(0,len(unique_journals)):
    unique_journals[i] = unique_journals[i].replace('MIT Press Journals','')
    
# finally, display them all
for i in range(0,len(unique_journals)):
    print(unique_journals[i] + ' | ' + unique_feeds[i])
