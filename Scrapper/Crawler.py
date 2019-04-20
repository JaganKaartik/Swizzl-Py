#Google News RSS/XML Crawler 

from bs4 import BeautifulSoup
import requests
import time
start = time.time()

text = input("Enter search query : ")
htmlurl = 'https://news.google.com/rss/search?q='+text
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

feedDict = {}
te = []

for i in titles:
	te.append(i.get_text())
	feedDict['title'] = te
te = []
for i in links:
	te.append(i.get_text())
	feedDict['link'] = te
te = []
for i in pubDates:
	te.append(i.get_text())
	feedDict['pubdate'] = te
te = []
for i in descriptions:
	string = i.get_text()
	string = string.split('<p>')[1]
	string = string[:-4]
	te.append(string+"Read More")
	feedDict['description'] = te

print(feedDict['title'][0])
print(feedDict['link'][0])	
print(feedDict['pubdate'][0])
print(feedDict['description'][0])

end = time.time()
print("Execution Time : ",end - start)



#Ref: http://www2.hawaii.edu/~takebaya/cent110/xml_parse/xml_parse.html


#Ref: Life Saver http://blog.thehumangeo.com/2015/07/09/no-soup-for-you-when-beautiful-soup-doesnt-like-your-xml/