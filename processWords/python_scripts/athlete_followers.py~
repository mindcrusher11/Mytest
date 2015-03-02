from authenticate_twitter import authenticate_user
from user_location import get_user_location
from address_coordinates import decode_address_to_coordinates
from broadband import decode_broadband_map_coordinates
import user_location as ul
import json,time
import mongo_crud as mg
import geopy_test as gp
import tweepy
import authenticate_twitter as at
from thread import start_new_thread

api_test = at.authenticate_test_app()
api_athlete = at.authenticate_api_athlete()
api_frank = at.authenticate_api_frank()
api = authenticate_user()
api_frank_1 = at.autheticate_api_frank_1()
db = mg.connect_to_server('localhost',27017,'dma')
twitterIdCollection = db.twitter_url
followerCollection = db.followers_info

def get_dma_values(api, user_id):
	#try:
		user_location = get_user_location(api, user_id).encode('utf-8')

		user_coordinates = decode_address_to_coordinates(user_location)
	
		print(user_coordinates)
		print('location is ', user_location)

		#if(user_location != '' and user_coordinates != None and user_location != None):
		#	print(user_coordinates['lat'],user_coordinates['lng'])

		#	print('before broadband')
		#	if 'lat' in user_coordinates:
		#		cop = str(user_coordinates['lat']) + ',' + str(user_coordinates['lng'])
		#		print('cop value is ',cop)
		#		response = gp.reverse_coordinates(cop)
				#response = decode_broadband_map_coordinates(user_coordinates['lat'],user_coordinates['lng'])
				#print('response is ',response)
	#except:
		#print('exception occured in get_dma_values')

def save_athlete_followers():
	#try:
		urls = twitterIdCollection.find({'link':{'$regex':'AthleteID='},'twitter_url_link':{'$ne':None},'followers':None})
		for url in urls:
			#print(url)
			screen_name = url['screen_name']
			#time.sleep(30)
			followers = ul.get_followers(api,screen_name)
			time.sleep(30)
			twitterIdCollection.update({'twitter_url_link': url['twitter_url_link']},{'$set':{'followers':followers}})
			time.sleep(30)
			#for follower_id in followers:
				#print(follower_id)
			#print(screen_name)
			#ul.get_followers(api,)
			#print(url['twitter_url_link'])
	#except:
		#print('exception occured in save_athlete_followers')



def save_mitch_followers(api,url_link):
	screen_name = url_link.replace('https://twitter.com/','')
	screen_name = screen_name.rstrip()
	followers = ul.get_followers(api,screen_name)
	twitterIdCollection.update({'twitter_url_link': url_link},{'$set':{'screen_name':screen_name,'followers':followers}})

def save_screen_name(api):
	urls = twitterIdCollection.find({'link':{'$regex':'AthleteID='},'twitter_url_link':{'$ne':None},'followers':None})
	for url in urls:
		print(url)
		screen_name = url['twitter_url_link'].replace('https://twitter.com/','')
		screen_name = screen_name.rstrip()
		twitterIdCollection.update({'twitter_url_link': url['twitter_url_link']},{'$set':{'screen_name':screen_name}})

def save_followers(api,screen_name):
	followers_list = followerCollection.find({'follower_id':{'$ne':None}},{'follower_id':True,'_id':False})
	listFollowers = twitterIdCollection.find({'screen_name':screen_name},{'followers':True,'_id':False})
	#listFollowers = find_followers(api, "Ayush_Flint")

	for listfol in listFollowers:
		for user_id in listfol['followers']:
			user_location = get_user_location(api, user_id)
			if(user_location != ''):
				user_location = user_location.encode('utf-8')
			print(user_location)
			user_location = ''
			follower_data = {'follower_id':user_id,'following':screen_name,'location':user_location}
			followerCollection.insert(follower_data)
			#get_dma_values(api,i)
			time.sleep(10)

def save_followers_test(api,screen_name):
	followers_list = db.follower_test.find({'location':None})

	for listfol in followers_list:
		user_id = listfol['follower_id']
		user_location = get_user_location(api, user_id)
		user_location = user_location.encode('utf-8')
		print(user_location)
		follower_data = {'follower_id':user_id,'following':screen_name,'location':user_location}
		db.follower_test.update({'follower_id':user_id},{'$set':{'location':user_location}})
		#time.sleep(10)

def save_followers_only(api,screen_name):
	listFollowers = twitterIdCollection.find({'screen_name':screen_name},{'followers':True,'_id':False})
	for listfol in listFollowers:
		for user_id in listfol['followers']:
			db.follower_test.update({'follower_id':None},{'follower_id':user_id,'following':screen_name},upsert=True)
			#db.follower_test.update({'follower_id':user_id},{'following':screen_name},upsert=True)

count = 0
def save_follower_screen_name(api):
	try:
		urls = db.follower_test.find({'screen_name':None,'follower_id':{'$ne':2178759026}},{'_id':False})
		count = 0
		for url in urls:	
			count = count + 1		
			print(count)
			if(count == 100):
				time.sleep(100)
				count = 0
			print(url)
			screen_name = ul.get_screen_name(api,url['follower_id'])
			screen_name = screen_name.rstrip()
			is_geo_enabled = ul.get_geo_location(api,screen_name)
			db.follower_test.update({'follower_id': url['follower_id']},{'$set':{'screen_name':screen_name,'is_geo_enabled':is_geo_enabled}})
		return True
	except:
		print("exception occurred in save_follower_screen_name")
		time.sleep(80)
		return save_follower_screen_name(api)
		


def save_athlete_followers_id(user_id):
	#try:
			screen_name = ul.get_screen_name(api,user_id)
			is_geo_enabled = ul.get_geo_location(api,screen_name)
			followers = ul.get_followers(api,screen_name)
			#time.sleep(30)
			db.follower_test.update({'follower_id': user_id},{'$set':{'followers':followers,'screen_name':screen_name,'is_geo_enabled':is_geo_enabled}})
			time.sleep(30)
			#for follower_id in followers:
				#print(follower_id)
			#print(screen_name)
			#ul.get_followers(api,)
			#print(url['twitter_url_link'])
	#except:
		#print('exception occured in save_athlete_followers')

def save_user(api):
	try:
		urls = db.follower_test.find({'user':None},{'_id':False})
		count = 0
		for url in urls:	
			count = count + 1		
			#print(count)
			if(count == 100):
				time.sleep(100)
				count = 0
			#print(url)
			user = ul.get_user(api,url['follower_id'])
			#print(user)
			if(user != None and user._json != None):
				user = user._json
			#print(user)
			#screen_name = screen_name.rstrip()
			#is_geo_enabled = ul.get_geo_location(api,screen_name)
				db.follower_test.update({'follower_id': url['follower_id']},{'$set':{'user':user}})
			#print("saved")
		return True
	except:
		print("exception occurred in save_user")
		time.sleep(180)
		return save_user(api)

def save_active_user(api):
	try:
		urls = db.active_athletes.find({'Twitter_username':{'$ne':""}})
		count = 0
		for url in urls:	
			count = count + 1		
			#print(count)
			#if(count == 100):
			#	time.sleep(100)
			#	count = 0
			#print(url)
			user = ul.get_user(api,url['Twitter_username'])
			#print(user)
			if(user != None and user._json != None):
				user = user._json
			#print(user)
			#screen_name = screen_name.rstrip()
			#is_geo_enabled = ul.get_geo_location(api,screen_name)
				db.active_athletes.update({'Twitter_username': url['Twitter_username']},{'$set':{'user':user}})
			#print("saved")
		return True
	except:
		print("exception occurred in save_user")
		time.sleep(60)
		return save_active_user(api)

save_active_user(api_frank_1)

start_new_thread(save_active_user,(api,))
start_new_thread(save_active_user,(api_frank,))
start_new_thread(save_active_user,(api_athlete,))
start_new_thread(save_active_user,(api_test,))

c = raw_input("Type something to quit")

#save_athlete_followers_id(2993863914)

#save_follower_screen_name(api_frank)

#save_followers_only(api,'mitchrichmond23')
#save_followers_test(api,'mitchrichmond23')

#save_screen_name(api)

#save_mitch_followers(api,"https://twitter.com/HasheemTheDream")
#save_athlete_followers()

#print(user_location.get_user(api,"JoeJohnson"))
#print(user_location.get_screen_name(api, "JoeJohnson"))

#listFollowers = twitterIdCollection.find({'screen_name':'mitchrichmond23'},{'followers':True,'_id':False})
#listFollowers = find_followers(api, "Ayush_Flint")

#for listfol in listFollowers:
#	for i in listfol['followers']:
#		follower_data = {'follower_id':i,'following':screen_name}
#		get_dma_values(api,i)
#		time.sleep(10)


#for status in tweepy.Cursor(api.user_timeline,id="mitchrichmond23").items(2): 
#	print status

#get_dma_values(api, '186878273')




