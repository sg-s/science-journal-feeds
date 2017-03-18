# scrapes Oxford university press and returns a list of feeds
# get the main page
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://academic.oup.com/journals/pages/journals_a_to_z").read().decode('utf-8')

# get all links from this page

soup = BeautifulSoup(html, 'html.parser')
all_journal_links = []
all_journal_names = []
for link in soup.find_all('a'):
    all_journal_links.append(link.get('href'))
    all_journal_names.append(link.get_text())
jl = [x for x,y in zip(all_journal_links, all_journal_names) if x is not None]
jn = [y for x,y in zip(all_journal_links, all_journal_names) if x is not None]
all_journal_names = jn
all_journal_links = jl
jl = [x for x,y in zip(all_journal_links, all_journal_names) if x.find('https://academic.oup.com/') > -1 and x.find('journals') == -1]
jn = [y for x,y in zip(all_journal_links, all_journal_names) if x.find('https://academic.oup.com/') > -1 and x.find('journals') == -1]
all_journal_names = jn
all_journal_links = jl

# now add /issuue/ to each of these, that is the correct link with the RSS link
all_journal_links = [x.strip() + '/issue/' for x in all_journal_links]

rss_links = [None]*len(all_journal_links)
for i in range(0,len(all_journal_links)):
    this_link = all_journal_links[i]
    html = urlopen(this_link).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    all_links = soup.find_all('a')
    for j in range(0,len(all_links)):
        if all_links[j].get_text().find('RSS Feed - Current Issue Only') > -1:
            rss_links[i] = all_links[j].get('href')
            print(all_journal_names[i] + " | " + rss_links[i])
