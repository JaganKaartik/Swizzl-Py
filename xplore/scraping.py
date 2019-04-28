#Google News RSS/XML Crawler

from bs4 import BeautifulSoup
import requests
import json
#import time
#start = time.time()

#text = input("Enter search query : ")

def scrape():
    htmlurl = 'https://news.google.com/rss/search?q=sports'
    url = requests.get(htmlurl)
    soup = BeautifulSoup(url.text,'xml')

    titles = soup.findAll('title')
    titles.pop(0)

    links = soup.findAll('link')
    links.pop(0)

    pubDates = soup.findAll('pubDate')
    pubDates.pop(0)

    descriptions = soup.findAll('description')
    descriptions.pop(0)

    #Dictionary to hold crawled information

    GfeedDict = {}
    te = []

    for i in titles:
        te.append(i.get_text())
        GfeedDict['title'] = te
    te = []
    for i in links:
        te.append(i.get_text())
        GfeedDict['link'] = te
    te = []
    for i in pubDates:
        te.append(i.get_text())
        GfeedDict['pubdate'] = te
    te = []
    for i in descriptions:
        string = i.get_text()
        string = string.split('<p>')[1]
        string = string[:-4]
        te.append(string+"Read More")
        GfeedDict['description'] = te

    #y = json.dumps(GfeedDict)
    return GfeedDict

    """
    GfeedDict = {
        'title':list
        

    }
    """


#end = time.time()
#print("Execution Time : ",end - start)



#Ref: http://www2.hawaii.edu/~takebaya/cent110/xml_parse/xml_parse.html


#Ref: Life Saver http://blog.thehumangeo.com/2015/07/09/no-soup-for-you-when-beautiful-soup-doesnt-like-your-xml/

if __name__ == "__main__":
    print(scrape())
