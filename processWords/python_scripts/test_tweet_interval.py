import tweepy
import json
import urllib, urllib2, json
from pygeocoder import Geocoder 
import mongo_crud as mg
import time


db = mg.connect_to_server('localhost',27017,'dma')
active_player = db.active_athletes

consumer_key="hhYq78kZ6VkAp4Q4pXzuKCOkA"
consumer_secret="A468W3FnFd9WcL2PXYeRO0iLWnu90761HkKHijXRXqmgtR1bpk"
access_token="374363728-BCe1rusHWiVPBHDCQ5RoketbfaNePuHXTeJja7W6"
access_token_secret="cMyNaQwVzxtXKqSG0jjlI1H6avEoMbvZ36pB7Zr5dPEN0"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

def save_tweets_excep(player):
	#try:
		#query_player = str(player) + ' ' + 'nba'  + ' since:2014-08-01 until:2014-12-01 , nba , ' + str(player) 
		query_player = str(player) + ' since:2014-08-01 until:2014-12-01 , nba' 
		query_player = str(player) + ' until:2014-12-01'
		query_player = str(player) + ' ' + 'nba'  + ' OR nba OR ' + str(player)
		query_player = str(player) + ' until:2014-12-01'
		query_player = str(player)
		print(query_player) 

		for tweet in tweepy.Cursor(api.search,q=query_player,until='2014-08-23',f='realtime',src='typd').items():
			#db.player_tweets.insert({'Player':player,'tweet_text':tweet.text,'tweet':tweet})
			#db.player_tweets.insert({'Player':player,'tweet_text':tweet.text,'location':tweet.user.location,'tweet':tweet._json})
			db.player_tweets_interval.insert({'Player':player,'tweet_text':tweet.text,'location':tweet.user.location, 'created_date':tweet.created_at})			
			print '***********************************'
			print('text is ',tweet.created_at)
			#print('co ordinates are ',tweet.geo)
			print '***********************************'
			print('text is ',tweet.text.encode("utf-8"))
			#print '***********************************'	
			#print('place is ',tweet.place)
			#print '***********************************'
			#print('country code is',tweet.place.country_code)
			#print '***********************************'
			#print('place full name is',tweet.place.full_name)
			#print '***********************************'
			#print('location is ',tweet.user.location)
			#print '***********************************'
			#print('tweet is ',tweet)
		return True
	#except:
	#	print('exception caught')
	#	time.sleep(60)
	#	return save_tweets_excep(player)


save_tweets_excep('Akil Mitchell')
