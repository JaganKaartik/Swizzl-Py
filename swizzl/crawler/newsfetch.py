"""

	This is the updated News Fetcher for Swizzl

"""

from bs4 import BeautifulSoup
import requests 

"""
	linkText(link)
	This is the function that retrives text data from the "links" fetched from other rss crawlers

"""

def linkText(link):
	url = "{}".format(link)
	r = requests.get(url) 
	soup = BeautifulSoup(r.content,"lxml") 
	article_text = ''
	mylink = soup.find('div').findAll('p')
	for i in mylink:
		article_text += ''.join(i.findAll(text = True))
	return article_text

def YahooFetch():
    url = "https://news.yahoo.com/rss/"
    url = requests.get(url)
    soup = BeautifulSoup(url.text,'xml')
    
    try:
        # Fetch All Required items

        titles = soup.findAll('title')
        links = soup.findAll('link')
        pubDates = soup.findAll('pubDate')

    except Exception as e :
        # Return Empty if titles, links, descriptions, pubdates not found
       
        print(e)
        return "Error"

    # We don't want the first elements as these are just metadata
    
    titles.pop(0)
    titles.pop(0)
    links.pop(0)
    links.pop(0)
    pubDates.pop(0)

    #Dictionary to hold crawled information

    FeedDict = {}
    temp = []
    temptext = []
    try:
        for i in titles:
            temp.append(i.get_text())
            FeedDict['title'] = temp
        temp = []
        for i in links:
            temp.append(i.get_text())
            temptext.append(linkText(i.get_text()))
            FeedDict['link'] = temp
            FeedDict['linktext'] = temptext
        temp = []
        for i in pubDates:
            temp.append(i.get_text())
            FeedDict['pubdate'] = temp
        
        print("Success")
    except Exception as e :
        print(e)
        return "Error"
    
    return FeedDict

