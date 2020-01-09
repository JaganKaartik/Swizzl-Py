"""

	This is the updated News Fetcher for Swizzl

"""

from bs4 import BeautifulSoup
import requests 
from swizzl.services.mlearning import sentiment as st
from swizzl.services.mlearning import prof
import re
import html
import nltk
nltk.download('vader_lexicon')

"""
	linkText(link)
	This is the function that retrives text data from the "links" fetched from the yahoo fetch rss crawler

"""
def linkImg(link):
    url = "{}".format(link)
    r = requests.get(url) 
    soup = BeautifulSoup(r.content,"lxml") 
    obj = soup.find_all("img",class_="Maw(100%)")
    for i in obj:
        return i['src']

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
    
    
    try:
        # Add titles to the Dictionary
        
        for i in titles:
            temp.append(html.unescape(i.get_text()))
            FeedDict['title'] = temp
            
        # Add link and details regarding text contetn @ link to the Dictionary
        
        temp = []
        temptext = []
        tbscore = []
        vadscore = []
        profvalue = []
        for i in links:
            
            # Append Links
            temp.append(html.unescape(i.get_text()))
            
            # Append Text Content from Links
            textval = linkText(html.unescape(i.get_text()))
            textval = re.sub('\"','\\"',textval)
            textval = " \" " + textval + " \" "
            
            #Run LinkImg Finder
            temptext.append(linkImg(html.unescape(i.get_text())))
            
            # Find Subjectivity, Objectivity of text content
            score = st.sentimentTB(textval)
            tbscore.append(score)
            
            # Find Sentiment of text content
            score = st.sentimentVader(textval)
            vadscore.append(score)
            
            # Find Profanity Score of content
            textval = [textval]
            score = float(prof.predProf(textval))
            profvalue.append(score)
            
            # Add to Feeds Dictionary 
            FeedDict['link'] = temp
            FeedDict['linktext'] = temptext
            FeedDict['tbScore'] = tbscore
            FeedDict['vaderScore'] = vadscore
            FeedDict['prof'] = profvalue
            
        # Add Published Dates to the Dictionary
        temp = []
        for i in pubDates:
            temp.append(i.get_text())
            FeedDict['pubdate'] = temp
        
        print("Success")
    except Exception as e :
        print(e)
        return "Error"
    
    return FeedDict

"""

*Testing Purposes*

Print FeedDict in this format 

print(FeedDict['title'][0])
print(FeedDict['link'][0])
print(FeedDict['linktext'][0])
print(FeedDict['pubdate'][0])

Crawler tested and verified using Jupyter Notebook

"""
