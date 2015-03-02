import pymongo
from pymongo import MongoClient


def connect_to_server(server_name,port_number,db=None):
	client = MongoClient(server_name,port_number)
	if(db != None):	
		return client[db]
	else:
		return client



#print connect_to_server('localhost',27017,'dma')

def remove_duplicates(collection,index_key):
	collection.ensureIndex({index_key:1},{'unique':'true','dropDups':'true'})
