with open('sd.csv') as f:
    content = f.readlines()
    
journal_names = []
feed_links = []
rss_root = 'http://rss.sciencedirect.com/publication/science/'
for i in range(0,len(content)):
    thisline = content[i]
    if thisline.find('Journal') > -1 and thisline.find('No longer published') == -1:
        a = thisline.find('http://www.sciencedirect.com/science/journal')
        z = thisline[a:].find(',')
        journal_id = thisline[a+45:a+z] 
        this_feed = rss_root+journal_id
        if this_feed not in feed_links:
            journal_names.append(thisline[0:thisline.find(',')])
            feed_links.append(this_feed)
        
for i in range(0,len(feed_links)):
    print(journal_names[i] + " | " + feed_links[i])