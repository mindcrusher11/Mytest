import tweepy
import time


def get_user(api, user_name):
	try:
		user = api.get_user(user_name)	
		return user
	except:
		return None

def get_user_location(api, user_name):
	try:
		print(user_name)
		user = api.get_user(user_name)
		#print(user)
		#print('loc is ', user.location)
		location = user.location
		return location
	except:
		print('exception occured')
		return get_user_location(api, user_name)
		#return None

def get_follower_count(api, user_name):
	try:
		user = api.get_user(user_name)
		follower_count = user.followers_count
		return follower_count
	except:
		return None


def get_screen_name(api, user_name):
	try:
		user = api.get_user(user_name)
		return user.screen_name
	except:
		print('exception occured in get screen name function')
		time.sleep(100)
		return get_screen_name(api, user_name)
	#	return None

def get_followers(api,user_screen_name):
	#try:
		ids = []
		for page in tweepy.Cursor(api.followers_ids, screen_name=user_screen_name).pages():
	    		ids.extend(page)
	    		time.sleep(30)
		return ids
	#except:
		#print('exception occurred in get_followers')


def get_geo_location(api,user_id):
	try:
		user = api.get_user(user_id)
		return user.geo_enabled
	except:
		print('exception occured in get screen name function')
		return get_geo_location(api,user_id)
