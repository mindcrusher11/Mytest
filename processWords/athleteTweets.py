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



import itertools


#def paginate(iterable, page_size):
#    while True:
#        i1, i2 = itertools.tee(iterable)
#        iterable, page = (itertools.islice(i1, page_size, None),
#                list(itertools.islice(i2, page_size)))
#        if len(page) == 0:
#            break
#        yield page


#c = tweepy.Cursor(api.followers_ids, screen_name = "QuincyAcy")
#ids = []
#for page in c.pages():
#     ids.append(page)

#print(followers)
#for page in paginate(ids, 100):
#    results = api.lookup_users(user_ids=page)
#    for result in results:
#        print result.screen_name

#for follower in api.followers_ids('twitter'):
 #   print api.get_user(follower).screen_name

# If the authentication was successful, you should
# see the name of the account print out

#user = api.followers(["Quincy Acy"][-1])
#print(user.)

for user in tweepy.Cursor(api.followers, screen_name="QuincyAcy").items():
    print user.screen_name

#for block in tweepy.Cursor(api.followers_ids, "Quincy Acy").items():
#	print block


