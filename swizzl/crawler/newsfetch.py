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
    Required

    <item>
    	<title>
    	<description>
		<link>
		<pubDate>
	</item>
    """
