from geopy.geocoders import Nominatim

geolocator = Nominatim()

def geo_test():
	location = geolocator.geocode("175 5th Avenue NYC")
	print(location.address)
	print(location.latitude,location.longitude)
	print(location.raw)

def reverse_coordinates(coordinates):
	location = geolocator.reverse(coordinates)	
	print(location.address)
	print(location.latitude,location.longitude)
	print(location.raw)	

#geo_test()
#reverse_coordinates()
