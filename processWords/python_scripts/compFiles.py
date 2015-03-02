with open('/home/hduser/libData/name.csv') as capName:
	lineset = set(capName)
with open('/home/hduser/libData/same','w') as out:
	for line in lineset:
		#print(line)
		out.write(line)

with open('/home/hduser/libData/brandsCol.csv') as brand:
	lineset.difference_update(brand)

with open('/home/hduser/libData/colorsCol.csv') as color:
	lineset.difference_update(color)

with open('/home/hduser/libData/materialsCol.csv') as material:
	lineset.difference_update(material)

with open('/home/hduser/libData/keyLib.csv') as key:
	lineset.difference_update(key)

with open('/home/hduser/libData/diff','w') as out:
	for line in lineset:
		#print(line)
		out.write(line)
