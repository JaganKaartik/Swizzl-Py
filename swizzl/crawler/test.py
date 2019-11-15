from bs4 import BeautifulSoup
import requests 

url = "https://news.yahoo.com/climate-change-damaging-health-worlds-233105120.html"
r = requests.get(url) 
soup = BeautifulSoup(r.content,"lxml") 

article_text = ''
mylink = soup.find('div').findAll('p')

for i in mylink:
	article_text += ''.join(i.findAll(text = True))

print(article_text)