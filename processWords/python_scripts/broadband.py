import urllib, urllib2, json
import pandas as pd

def read_xlsx_file_pandas(file_name,sheet_name):
	excel_file = pd.ExcelFile(file_name)
	parsedFile = excel_file.parse(sheet_name)
	try:
		return parsedFile
	except:
		return None 

def decode_broadband_map_coordinates(latitude,longitude):
	params = {
                'latitude' : latitude,
                'longitude' : longitude,
		'format' : 'json'
        }  
	try:
		url = 'http://www.broadbandmap.gov/broadbandmap/demographic/2012/coordinates?' + urllib.urlencode(params)
		response = urllib2.urlopen(url)
		result = json.load(response)
		print(result['Results']['incomeBetween100to200'])
		print(result['Results']['blockFips'])
		print(result['Results']['incomeLessThan25'])
		print(result['Results']['incomeBelowPoverty'])
		print(result['Results']['medianIncome'])
		print(result['Results']['incomeGreater200'])
		print(result['Results']['educationBachelorOrGreater'])
		print(result['Results']['incomeBetween50to100'])
		print(result['Results']['educationHighSchoolGraduate'])
		print(result['Results']['incomeBetween25to50'])
			
                return response
        except:
                return None


def process_data(data_frame):
	print(data_frame.columns)
	#print(data_frame['longitude'],'latitude is',data_frame['latitude'])
	try:
		for index,row in data_frame.iterrows():
			 response = decode_broadband_map_coordinates(row['latitude'],row['longitude'])
			 #print(row.keys())
			 #print(response)
			 if(response != None):
				 result = json.load(response)
				 #print(result)

				 #print('if incomeBetween100to200','incomeBetween100to200' in row.keys())
				 if('incomeBetween100to200' in row.keys() and 'incomeLessThan25' in result['Results'].keys()):
				 	data_frame.loc[index,'incomeBetween100to200'] = result['Results']['incomeBetween100to200']
				 else:
					data_frame.loc[index,'incomeBetween100to200'] = 'NA'

				 #print('if blockFips','"blockFips"' in row.keys())
				 if('"blockFips"' in row.keys() and 'blockFips' in result['Results'].keys()):
				 	data_frame.loc[index,'"blockFips"'] = result['Results']['blockFips']
				 else:
					data_frame.loc[index,'"blockFips"'] = 'NA'

				 #print('if incomeLessThan25','incomeLessThan25' in row.keys())
				 #print('if incomeLessThan25 ','incomeLessThan25' in row.keys() and 'incomeLessThan25' in result['Results'].keys())
				 if('incomeLessThan25' in row.keys()):
				 	data_frame.loc[index,'incomeLessThan25'] = result['Results']['incomeLessThan25']
				 else:
					data_frame.loc[index,'incomeLessThan25'] = 'NA'
				 
				 #print('if incomeBelowPoverty','"incomeBelowPoverty"' in row.keys())
				 if('"incomeBelowPoverty"' in row.keys() and 'incomeBelowPoverty' in result['Results'].keys()):
				 	data_frame.loc[index,'"incomeBelowPoverty"'] = result['Results']['incomeBelowPoverty']
				 else:
					data_frame.loc[index,'"incomeBelowPoverty"'] = 'NA'

				 #print('if medianIncome','medianIncome' in row.keys())
				 if('medianIncome' in row.keys()):
				 	data_frame.loc[index,'medianIncome'] = result['Results']['medianIncome']
				 else:
					data_frame.loc[index,'medianIncome'] = 'NA'

				 #print('if incomeGreater200','incomeGreater200' in row.keys())
				 if('incomeGreater200' in row.keys()):
				 	data_frame.loc[index,'incomeGreater200'] = result['Results']['incomeGreater200']
				 else:
					data_frame.loc[index,'incomeGreater200'] = 'NA'

				 #print('if educationBachelorOrGreater','educationBachelorOrGreater' in row.keys())
				 if('educationBachelorOrGreater' in row.keys()):
				 	data_frame.loc[index,'educationBachelorOrGreater'] = result['Results']['educationBachelorOrGreater']
				 else:
					data_frame.loc[index,'educationBachelorOrGreater'] = 'NA'

				 #print('if incomeBetween50to100','incomeBetween50to100' in row.keys())
				 if('incomeBetween50to100' in row.keys()):
				 	data_frame.loc[index,'incomeBetween50to100'] = result['Results']['incomeBetween50to100']
				 else:
					data_frame.loc[index,'incomeBetween50to100'] = 'NA'
				 
				 #print('if educationHighSchoolGraduate','educationHighSchoolGraduate' in row.keys())
				 if('educationHighSchoolGraduate' in row.keys()):
				 	data_frame.loc[index,'educationHighSchoolGraduate'] = result['Results']['educationHighSchoolGraduate']
				 else:
					data_frame.loc[index,'educationHighSchoolGraduate'] = 'NA'

				 #print('if incomeBetween25to50','incomeBetween25to50"' in row.keys())
				 if('incomeBetween25to50"' in row.keys()):
				 	data_frame.loc[index,'incomeBetween25to50"'] = result['Results']['incomeBetween25to50']
				 else:
					data_frame.loc[index,'incomeBetween25to50"'] = 'NA'
			 #write_to_data_frame(response)

		write_to_csv('/home/hduser/Desktop/processWords/dma/dma_demo.csv',data_frame)
	except:
		print('exception occured')

def write_to_csv(file_path,data_frame):
	data_frame.to_csv(file_path,)

def write_to_data_frame(json_response):
	result = json.load(json_response)
	print(result['Results']['incomeBetween100to200'])

#print decode_broadband_map_coordinates()
#xlsx_data_frame = read_xlsx_file_pandas('/home/hduser/DMA_Cities_Demographics.xlsx','53%')

#process_data(xlsx_data_frame)
