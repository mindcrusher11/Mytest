import pymongo
from pymongo import MongoClient


client = MongoClient()
client = MongoClient('localhost',27017)

db = client.dma
collection = db.masterdma
collectionAdwords = db.adwords

	#print('city is '+ dmaPosts['City'],'state is '+ dmaPosts['State']) 
def findadsinmaster():
	for dmaPosts in collectionAdwords.find().limit(10):
		#print('city is '+ dmaPosts['City'],'state is '+ dmaPosts['State'])
		#print collection.find({'City':'Galena','State':'Alaska'}).count()
		print collection.find_one({'City':dmaPosts['City'],'State':dmaPosts['State']})
	#print masterData


def updateMaster():
	for dmaPosts in collectionAdwords.find():
		print 'in for loop'
		collection.update({'City':dmaPosts['City'],'State':dmaPosts['State']},{'$set':{'DMA Region':dmaPosts['DMA Region Code']}},True,True)


#findadsinmaster()
#updateMaster()
