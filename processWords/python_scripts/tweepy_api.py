import tweepy
import json
import urllib, urllib2, json
from pygeocoder import Geocoder 


# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="hhYq78kZ6VkAp4Q4pXzuKCOkA"
consumer_secret="A468W3FnFd9WcL2PXYeRO0iLWnu90761HkKHijXRXqmgtR1bpk"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="374363728-BCe1rusHWiVPBHDCQ5RoketbfaNePuHXTeJja7W6"
access_token_secret="cMyNaQwVzxtXKqSG0jjlI1H6avEoMbvZ36pB7Zr5dPEN0"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
#api.update_status('Updating using OAuth authentication via Tweepy!')
#print api.search(geocode='33.5206608,-86.80248999999999,15')
#print api.rate_limit_status()


for tweet in tweepy.Cursor(api.search,q="Quincy Acy",lang="en",geocode="40.712784,-74.005941,10000mi").items(10):
	print '***********************************'
	print('co ordinates are ',tweet.geo)
	print '***********************************'
	print('text is ',tweet.text.encode("utf-8"))
	print '***********************************'	
	#print('place is ',tweet.place)
	#print '***********************************'
	print('country code is',tweet.place.country_code)
	print '***********************************'
	print('place full name is',tweet.place.full_name)
	print '***********************************'
	print('location is ',tweet.user.location)
	print '***********************************'
	print('tweet is ',tweet)



def decode_address_to_coordinates():
        params = {
                'lat' : '40.712784',
                'long' : '-74.005941',
        }  
        url = 'https://api.twitter.com/1.1/geo/reverse_geocode.json?' + urllib.urlencode(params)
        response = urllib2.urlopen(url)
        result = json.load(response)
        try:
                return result
        except:
                return None

#print decode_address_to_coordinates()

def decode_broadband_map_coordinates():
	params = {
                'lat' : '40.712784',
                'long' : '-74.005941',
        }  
        url = 'http://www.broadbandmap.gov/broadbandmap/demographic/2012/coordinates?' + urllib.urlencode(params)
        response = urllib2.urlopen(url)
        result = json.load(response)
        try:
                return result
        except:
                return None

