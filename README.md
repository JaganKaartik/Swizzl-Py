# Swizzl

## Introduction

Swizzl is a web application which aggregates syndicated web content from online newspapers, sources etc in one location for easy viewing. It can show new or updated information from websites. Visiting many separate websites frequently to find out if content on the site has been updated can take a long time. Aggregation technology helps to consolidate many websites into one page that can show the new or updated information from many sites. Aggregators reduce the time and effort needed to regularly check websites for updates, creating a unique information space or personal newspaper. It aims to remove all unwanted content, only displaying the relevant content. Once subscribed to a feed, an aggregator is able to check for new content at user-determined intervals and retrieve the update.

## Features of Swizzl

* Freshly Fetched Feeds from souces like (yahoonews, etc)
* Swizzl fetches relevant information along with the news content found in these links. [**Crawler**](https://github.com/JaganKaartik/Swizzl/blob/master/swizzl/services/newsfetch.py)
* Analysis such as the mentioned below are performed on these news content! 
    * Sentiment Analysis via ```VADER-Sentiment-Analysis```
    * Subjectivity and Objectivity measure from ```textBlob```
    * Profanity measure from ```profanity-check```
* Benefits include! Improved filtering of fetched feeds.
    * Eg. If a user needs only  ```+ve sentiment``` posts, the UI enables to toggle to view only such news.
    * Eg. If a user needs only  ```-ve sentiment``` posts, the UI enables to toggle to view only such news.
    * Eg. If a user needs both ```+ve sentiment```and ```-ve sentiment``` posts, the UI enables to view both such news.
    * Eg. If a user needs more subjective posts, the UI enables to toggle to view only such news.
    * Eg. If a user needs more objective posts, the UI enables to toggle to view only such news.
    * Eg. The ```predict_prob``` function from the profanity-check library, enables to predict the profanity content in the link text. A heuristic such as a threshold could be set to filter offensive content. If the user is a minor, existing profanity filter will toggle only SFW posts.
    
## Technology Stack

* Python ```3.6.5``` and above.
* Other python library dependencies specified in the ```requirements.txt```
* Celery Task Queue ```4.2```
* Redis-Server ```5.0.5```

## Instructions to use this Software

1. Change directory to project root ```/Swizzl```

2. Python Virtual Enviornment

    2.1. Create Python Virtual Enviornment by ```virtualenv "env name"``` here we have used "Swizzl" as the name of the virtual enviornment. So, type  ```virtualenv Swizzl```.
    
    2.2. Activate the virtual enviornment by ```source "env name"/bin/activate``` which is ```source Swizzl/bin/activate``` here. 

3. Start the Application

    ```python
       python run.py
    ``` 
   or  
    ```python
       export FLASK_APP=run.py
       flask run
    ```
4. Start the redis server by typing  ```redis-server``` in the terminal.

5. Start the celery task queue in another tab/terminal by typing
```
celery -A swizzl.routes:celery worker --loglevel=info
``` 
6. When ```\feeds``` link is visited inside the application, an asynchonous task is sent to the celery worker. 

7. Enjoy Reading :book: Cheers! :sunglasses:


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


#### Image Credits

[Photo by AbsolutVision on Unsplash](https://unsplash.com/photos/WYd_PkCa1BY)

[Photo by Alex Shutin on Unsplash](https://unsplash.com/photos/kKvQJ6rK6S4)

[Photo by Andreas Chu on Unsplash](https://unsplash.com/photos/YodH2WzN6YU)

[Photo by Chuttersnap on Unsplash](https://unsplash.com/photos/aku7Zlj_x_o)

[Photo by Harley-Davidson on Unsplash](https://unsplash.com/photos/56R8TzG7Lzc)

[Photo by Harley-Davidson on Unsplash](https://unsplash.com/photos/bs1eqd6zSiU)

