import tweepy
from textblob import TextBlob 
consumer_key = 'GJw3GCCixfA2QHLhHhZvhQbye'
consumer_secret = 'mtkvoux8ta9i5bKkl78RpfylH8oqt6askCA59eP6LLpJ1a0ZVf'

access_token = '2617710074-kqJ3PjLcBs5GqIJwfof7ipExHPgKBQBjfkwEpUK'
access_token_secret = 'jYjKqKvdOwRgPY4Dv0jy1i4qmSxSDyJUthjhHIkJ9wk7P'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Trump')
text_list = []
analysis_dict = dict()

for tweet in public_tweets :
	text_list.append(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
print(text_list)






