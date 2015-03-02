import string

wordFile = open("/home/hduser/Desktop/processWords/abc.csv",'r+')
keyWordFile = open("/home/hduser/Desktop/processWords/keyLib.csv","r+")

keywordfilelist = []
wordfilelist = []

for line in keyWordFile:
	keywordfilelist.append(line.strip())
	

for item in wordFile:
	wordfilelist.append(item.strip())

print(keywordfilelist)
print(wordfilelist)
for product in wordfilelist:
	if product in keywordfilelist:
		print "yes", product



wordFile.close()
keyWordFile.close()
