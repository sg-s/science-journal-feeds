# get the BMC web page
from urllib.request import urlopen
html = urlopen("http://www.biomedcentral.com/journals-a-z").read().decode('utf-8')

# get all links from this page
from bs4 import BeautifulSoup
import pdir
soup = BeautifulSoup(html, 'html.parser')
all_links = []
for link in soup.find_all('a'):
    all_links.append(link.get('href'))
    
all_links = [x for x in all_links if x.find('.biomedcentral') > -1 and x.find('http') == -1]

# clean up the links
for i in range(0,len(all_links)):
    all_links[i] = all_links[i].replace('//','http://')
    

# for each of these links, follow them, and look in that page if there is a RSS feed button 
import http.cookiejar
import urllib.request
import time
all_journal_names = []
all_feeds = []
for i in range(0,len(all_links)):
    this_link = all_links[i]    
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(this_link)
    html = r.read()
    soup = BeautifulSoup(html, 'html.parser')
    this_journal_name = soup.title.string
    this_journal_name = this_journal_name.replace('|',' ')
    this_feed = 'no-feed'
    for link in soup.find_all('a'):
        if link.get('href').find('rss') > -1:
            this_feed = link.get('href')
            time.sleep(1)
            this_feed = all_links[i] + this_feed
            all_feeds.append(this_feed) 
            this_journal_name = this_journal_name.replace('Home page','')
            all_journal_names.append(this_journal_name)
            print(this_journal_name)
            print(this_feed)
            
# skip the most accessed, we only care about most-recent 
recent_feeds = []
recent_journals = []
for i in range(0,len(all_feeds)):
    if all_feeds[i].find('most-recent') > -1:
        recent_feeds.append(all_feeds[i])
        recent_journals.append(all_journal_names[i])
        
# finally, display them all
for i in range(0,len(recent_journals)):
    print(recent_journals[i] + ' | ' + recent_feeds[i])