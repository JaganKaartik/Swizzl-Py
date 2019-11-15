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

	# Using Yahoo News RSS Feeds

	url = "https://news.yahoo.com/rss/"
	url = requests.get(url)
    soup = BeautifulSoup(url.text,'xml')

    """
    Required items to fetch

    <item>
    	<title>
    	<description>
		<link>
		<pubDate>
	</item>

    """

    try:
        # Fetch All Required items

        titles = soup.findAll('title')
        links = soup.findAll('link')
        descriptions = soup.findAll('description')
        pubDates = soup.findAll('pubDate')

    except Exception as e :
        # Return Empty if titles, links, descriptions, pubdates not found
        print(e)
        return "Error"

   	# We don't want the first elements as these are just metadata
    titles.pop(0)
    links.pop(0)
    pubDates.pop(0)
    descriptions.pop(0)

    # Dictionary to hold crawled information

    FeedDict = {}
    temp = []
    try:
        for i in titles:
            temp.append(i.get_text())
            FeedDict['title'] = temp
        temp.clear()
        for i in links:
            temp.append(i.get_text())
            FeedDict['link'] = temp
        temp.clear()
        for i in pubDates:
            te.append(i.get_text())
            FeedDict['pubdate'] = temp
        temp.clear()
       
    except Exception as e :
        print(e)
        return "Error"

    return FeedDict
