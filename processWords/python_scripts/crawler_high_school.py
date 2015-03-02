from bs4 import BeautifulSoup
import urllib2,string,re,time,json
import mongo_crud as mg
import pymongo as pym
from re import findall
import time

db = mg.connect_to_server('localhost',27017,'dma')
crawl_player = db.crawl_by_school_info_insert
element_list = []

def getCityUrls(url):
	try:
		state_url = urllib2.urlopen(url)
		birth_place_html = state_url.read()
		state_url.close()

		parse_html = BeautifulSoup(birth_place_html)
		#get_table = parse_html.find_all("table",{"class":"nav_table no_highlight stats_table"})
		#parse_table = BeautifulSoup(get_table)
		get_rows = parse_html.find_all("td")
		#print('table is ',get_rows)
		#get_urls = get_table.find("a")
		#print('url is',get_urls)
		for url in get_rows:
			get_link = url.find('a')
			#get_p_text = url.text
			print(get_link)
			#print(get_p_text)
			if get_link != None:
				get_player_url(get_link.get('href'),get_link.string)

		return True
	except:
		print("exception caught in get city urls function")
		time.sleep(60)
		return getCityUrls(url)
		

def get_player_url(url,state_location):
	try:
		#print('url is ',url)
		#print('location is ',state_location)
		#print('inside get_player_url')
		player_url = urllib2.urlopen('http://www.basketball-reference.com' + url)
		player_html = player_url.read()
		player_url.close()
		
		parse_html = BeautifulSoup(player_html)
		
		get_table = parse_html.find("tbody")
		#get_table = parse_html.find("table",{"id":"stats"})
		#print('table is ',get_table)
		for all_rows in get_table.find_all('tr',{"class":""}):
			#for all_rows in get_table.findChildren('td',{'align':'left'}):
			#print('inside for loop of allrows')
			#child_list = all_rows
			#print(all_rows)
			get_children_rows(all_rows,url,state_location)
		#for child in get_table.findChildren('td',{'align':'left'}):
		#	print('children is ',child)
			#print("children is ",child)
			#get_player_info(child['href'])
		return True
	except:
		print('exception in parse_url function')
		time.sleep(60)
		return get_player_url(url,state_location)	

def get_children_rows(all_rows,url,state_location):
		#print('length is',len(all_rows.findChildren('td',{'align':'left'})))
		child_count = len(all_rows.findChildren('td',{'align':'left'}))
		if child_count == 3:
			child_list = all_rows.findChildren('td',{'align':'left'})
			player_name = child_list[0].find('a').string
			city = child_list[1].string
			school_name = child_list[2].string

			state = state_location
			player_url = 'http://www.basketball-reference.com' + child_list[0].find('a')['href']
			state_url = 'http://www.basketball-reference.com' + url
			#print(child_list[0].find('a')['href'])		
			#print(child_list[0].find('a').string)
			#print(child_list[1].string)
			#print(child_list[2].string)
			#crawl_player.update({'name':player_name},{'$set':{'school_name' : school_name,'city':city,'state':state,'player_url':player_url,'state_url':state_url}},True)
			crawl_player.insert({'school_name':school_name,'city':city,'state':state,'player_url':player_url,'state_url':state_url})

getCityUrls("http://www.basketball-reference.com/friv/high_schools.cgi")

