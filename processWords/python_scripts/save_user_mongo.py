import mongo_crud as mg
import json

db = mg.connect_to_server('localhost',27017,'dma')

def save_user(collection_name):
	users = collection_name.find({'user':{'$ne':None}},{'user':True,'_id':False,'follower_id':True})
	for user in users:
		parse_user(user['user'])
		user_info = user['user']
		collection_name.update({'follower_id':user['follower_id']},{'$set':{'utc_offset':user_info['utc_offset'],'statuses_count':user_info['statuses_count'],'friends_count':user_info['friends_count'],'location':user_info['location'],'geo_enabled':user_info['geo_enabled'],'name':user_info['name'],'favourites_count':user_info['favourites_count'],'time_zone':user_info['time_zone']}})



def parse_user(user):
	#user_info = json.load(user)
	user_info = user	
	print("##################################")
	print('offset is ',user_info['utc_offset'])
	print('status count is ',user_info['statuses_count'])
	print('friends count is ',user_info['friends_count'])	
	print('location is ',user_info['location'])
	print('geo enable is ',user_info['geo_enabled'])
	print('name is ',user_info['name'])
	print('favourites count is ',user_info['favourites_count'])
	print('time zone is ',user_info['time_zone'])
	#print(user_info.)
	#print(user_info.)
	#print(user_info.)
	#print(user_info.)
	#print(user_info.)

save_user(db.follower_test)
