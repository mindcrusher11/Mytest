from bs4 import BeautifulSoup
import urllib2,string,re,time
import mongo_crud as mg
import pymongo as pym

import twitter

consumer_key="hhYq78kZ6VkAp4Q4pXzuKCOkA"
consumer_secret="A468W3FnFd9WcL2PXYeRO0iLWnu90761HkKHijXRXqmgtR1bpk"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="374363728-BCe1rusHWiVPBHDCQ5RoketbfaNePuHXTeJja7W6"
access_token_secret="cMyNaQwVzxtXKqSG0jjlI1H6avEoMbvZ36pB7Zr5dPEN0"

api = twitter.Api(consumer_key,
                      consumer_secret,
                      access_token,
                      access_token_secret)


#api.search.tweets(q='keyword')



	#def get_person_class():
	#	athlete_file = urllib2.urlopen("https://twitter.com/search?q=Akil%20Mitchell%20since%3A2014-12-08%20until%3A2015-02-01&src=typd")
		

#http://topsy.com/s?q=Akil%20Mitchell&mintime=1417980630&maxtime=1420486230

def get_urls():
	try:
		redditFile = urllib2.urlopen("http://topsy.com/s?q=Akil%20Mitchell&mintime=1417980630&maxtime=1420486230")
		redditHtml = redditFile.read()
		redditFile.close()

		soup = BeautifulSoup(redditHtml)
		redditAll = soup.find_all("a")
		print soup
		#for links in soup.find_all('a'):
		#	twitterIdCollection.update({'link':links.get('href')},{'$set':{'link':links.get('href')}},True,True)
			#twitterIdCollection.insert({'link':links.get('href')})
			#print(links.get('href'))
			#athlete_link = find_value('index.cfm?AthleteID=', links.get('href'))
			#twitterIdCollection.insert({'link':athlete_link})
			#if(athlete_link != ''):	
			#	twitterIdCollection.insert({'link':athlete_link})	
				#print(athlete_link)
				#athlete_list.append(athlete_link)
			#athlete_list.append(athlete_link) 
			#print(find_value('index.cfm?AthleteID=', links.get('href')))		
	except:
		print('exception occured in get_urls')

get_urls()