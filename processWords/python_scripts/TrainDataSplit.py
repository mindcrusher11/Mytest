import string

nameStringFile = open("/home/hduser/Desktop/processWords/TrainDataName.csv",'r+')

csvNameFile = open("/home/hduser/Desktop/processWords/csvNameFile.csv","w")

#for line in nameStringFile:
#	lineWords = line.split(" ")
#	for words in lineWords:
#		csvNameFile.write(words)
#		csvNameFile.write(",")


csvNameFile.close()

for line in nameStringFile:
	if 'beanies' in line:
		print line
