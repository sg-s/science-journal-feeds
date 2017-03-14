from urllib.request import urlopen
import listparser as lp
html = urlopen("http://cms.iopscience.iop.org/alfresco/d/d/workspace/SpacesStore/cd5bdf75-3373-11df-afda-57ea8c8155d6/iopscience-opml.xml?guest=true").read().decode('utf-8')
d = lp.parse(html)
journal_names = []
rss_feeds = []
feeds = d['feeds']
for i in range(0,len(feeds)):
    rss_feeds.append(feeds[i]['url'])
    this_title = feeds[i]['title']
    this_title = this_title.replace('latest articles','')
    journal_names.append(this_title)
    
for i in range(0,len(journal_names)):
    print(journal_names[i] + ' | ' + rss_feeds[i])

