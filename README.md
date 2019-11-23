# Swizzl

## Introduction

Swizzl is a web application which aggregates syndicated web content from online newspapers, blogs, etc in one location for easy viewing. It can show new or updated information from websites. This reduces the time and effort needed to regularly check websites for updates, also it creates a personalized information space. It aims to remove all unwanted content, only displaying the relevant content.


Visiting many separate websites frequently to find out if content on the site has been updated can take a long time. Aggregation technology helps to consolidate many websites into one page that can show the new or updated information from many sites. Aggregators reduce the time and effort needed to regularly check websites for updates, creating a unique information space or personal newspaper. Once subscribed to a feed, an aggregator is able to check for new content at user-determined intervals and retrieve the update.

## Swizzl UI 

### Login Page

![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/login.png)

### Register Page

![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/register.png)

### Home Page (Logged In)

![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/homePage.gif)

### Home Page (Explaining Features)

![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/f1.png)
![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/f2.png)
![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/f3.png)
![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/f4.png)
![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/f5.png)

### View Posts Page

![](https://github.com/JaganKaartik/Swizzl/blob/master/Documentation/Images/feedsPage.gif)

**Testing**

(Update: 21st November 2019)

#### How to run a celery task?

* Go to Directory ```/Swizzl```
* Run the redis server, ```redis-server```
* Run ```celery -A swizzl.routes:celery worker --loglevel=info``` 
* When ```\feeds``` link is visited, a async task is sent to the celery worker.

