# Swizzl

## Introduction

Swizzl is a web application which aggregates syndicated web content from online newspapers, sources etc in one location for easy viewing. It can show new or updated information from websites. Visiting many separate websites frequently to find out if content on the site has been updated can take a long time. Aggregation technology helps to consolidate many websites into one page that can show the new or updated information from many sites. Aggregators reduce the time and effort needed to regularly check websites for updates, creating a unique information space or personal newspaper. It aims to remove all unwanted content, only displaying the relevant content. Once subscribed to a feed, an aggregator is able to check for new content at user-determined intervals and retrieve the update.

## Features of Swizzl

* Freshly Fetched Feeds from souces like (yahoonews, etc)
* Swizzl fetches relevant information along with the news content found in these links. :sunglasses: [**Advanced Crawler**](https://github.com/JaganKaartik/Swizzl/blob/master/swizzl/services/newsfetch.py)
* Analysis such as the mentioned below are performed on these news content! 
    * Sentiment Analysis via ```VADER-Sentiment-Analysis```
    * Subjectivity and Objectivity measure from ```textBlob```
    * Profanity Scoring
* Benefits include! Improved filtering of fetched feeds.
    * Eg. If a user needs ```+ve sentiment``` posts, the UI enables to toggle to view only such news.
    * Eg. If a user needs more subjective posts, the UI enables to toggle to view only such news.
    * Eg. If the user is a minor, existing profanity filter will toggle only SFW posts.
    
## Swizzl UI 

### Login Page

![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/login.png)

### Register Page

![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/register.png)

### Home Page (Logged In) 
<small>*Takes time to load!</small>

![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/homePage.gif)

### Home Page (Explaining Features)

![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/f1.png)
![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/f2.png)
![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/f3.png)
![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/f4.png)
![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/f5.png)

### View Posts Page
<small>*Takes time to load!</small>

![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/feedsPage.gif)


## Testing

* The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective. The tbscore attribute keeps track of subjectivity.


#### How to run a celery task?

* Go to Directory ```/Swizzl```
* Run the redis server, ```redis-server```
* Run ```celery -A swizzl.routes:celery worker --loglevel=info``` 
* When ```\feeds``` link is visited, a async task is sent to the celery worker.

