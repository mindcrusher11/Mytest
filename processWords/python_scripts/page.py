import time
import tweepy

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

ids = []
def find_followers_page():
	current_cursor = ""
	for page in tweepy.Cursor(api.followers_ids, screen_name="QuincyAcy").pages():
	#current_cursor = cursor.iterator.next_cursor
		cursor = tweepy.Cursor(api.followers_ids, screen_name="QuincyAcy",  cursor =  current_cursor)
		current_cursor = cursor.iterator.next_cursor
		#print repr(cursor)
		#print current_cursor
		ids.extend(page)
		#print page
		time.sleep(20)
	return ids
#print find_followers()
#print('length of ids is ',len(ids))
#print("ids are ",ids)
