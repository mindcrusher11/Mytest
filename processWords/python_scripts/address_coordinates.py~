import urllib, urllib2, json
from pygeocoder import Geocoder 

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

def complete_result(address):
        params = {
                'address' : address,
                'sensor' : 'false',
        }  
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
        response = urllib2.urlopen(url)
        result = json.load(response)
        try:
                return result['results'][0]
        except:
                return None

def get_zipcode(address):
	try:
		result = Geocoder.geocode(address)
		isValid = result.valid_address
		print(isValid,'if valid or not')
		if isValid:
			print(address,' is valid address.')
		else:
			print(address,' is invalid address')
	
		print('postal code is ',result[0].postal_code)
		return result[0].postal_code
	except:
		return None

def get_address_using_coordinates(latitude,longitude):
	try:
		result = Geocoder.reverse_geocode(latitude, longitude)
		return result
	except:
		return None
	
#print decode_address_to_coordinates("Toronto")
#print decode_address_to_coordinates("Birmingham, AL")
#print decode_result('Toronto')
#print decode_result('Birmingham, AL')
print get_zipcode("451-499 24th Street North, Birmingham, AL 35203, USA")
print get_zipcode("Birmingham, AL")
address_la = decode_address_to_coordinates("Birmingham, AL")
print address_la

#result = get_address_using_coordinates(address_la['lat'],address_la['lng'])
#print result[0]
#print result[1]
#print result[2]
#print result[3]
#print result[4]
#print result[5]
#print result[6]
#print result[7]
#print result.country__short_name
#print result.postal_code
#print result.street_number
#print result.route
#print result.administrative_area_level_1
#print result.city
#print result.state
#print result.state__short_name
#print result.country
#print result.formatted_address
#print result.count
#print result.country__short_name
#print get_address_using_coordinates(address_co[0]['])
