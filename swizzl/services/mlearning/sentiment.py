from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

"""
	Using TextBlob Sentiment Scores to check for Subjectivity in text 
"""
def sentimentTB(text):
	blob = TextBlob(text)
	return blob.sentiment.subjectivity

"""
	Using Vader Sentiment Scores to retrive the overall Sentiment of the text
"""

def sentimentVader(text):
	nltk_sentiment = SentimentIntensityAnalyzer()
	score = nltk_sentiment.polarity_scores(text)
	return score
