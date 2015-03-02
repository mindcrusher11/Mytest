import urllib, urllib2, json, tweepy
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

def decode_address_to_coordinates(address):
        params = {
                'address' : address,
                'sensor' : 'false',
        }  
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
        response = urllib2.urlopen(url)
        result = json.load(response)
        try:
                return result['results'][0]['geometry']['location']
        except:
                return None

def decode_broadband_map_coordinates(latitude,longitude):
	params = {
                'latitude' : latitude,
                'longitude' : longitude,
		'format' : 'json'
        }  
	try:
		url = 'http://www.broadbandmap.gov/broadbandmap/demographic/2012/coordinates?' + urllib.urlencode(params)
		response = urllib2.urlopen(url)
		result = json.load(response)
		print(result['Results']['incomeBetween100to200'])
		print(result['Results']['blockFips'])
		print(result['Results']['incomeLessThan25'])
		print(result['Results']['incomeBelowPoverty'])
		print(result['Results']['medianIncome'])
		print(result['Results']['incomeGreater200'])
		print(result['Results']['educationBachelorOrGreater'])
		print(result['Results']['incomeBetween50to100'])
		print(result['Results']['educationHighSchoolGraduate'])
		print(result['Results']['incomeBetween25to50'])
			
                return response
        except:
                return None


user = api.get_user(screen_name="QuincyAcy")

print user.followers_count
print user.location
location =  decode_address_to_coordinates(user.location)

decode_broadband_map_coordinates(location['lat'],location['lng'])

