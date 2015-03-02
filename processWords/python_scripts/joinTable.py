import pandas as pd

u_cols = ['area', 'city']
partial = pd.read_csv('/home/hduser/Desktop/processWords/Partial _DMA.csv', names=u_cols)

#ad_cols = ['city','criteria','id','state','dma','region','dma1','region1','code']
#adwords = pd.read_csv('/home/hduser/AdWords API Cities-DMA Regions 2014-12-29 (4).csv', names=ad_cols)
#adwords = pd.read_csv('/home/hduser/AdWordsFiltered.csv',names=ad_cols)
ad_cols = ['City','criteria','id','state','dma','region']
adwords = pd.read_csv('/home/hduser/Desktop/processWords/AdWordsFiltered.csv',names=ad_cols)

r_cols = ['City', 'state', 'zipcode', 'state_code','latitude','longitude','dma_region']
#master = pd.read_csv('/home/hduser/Desktop/processWords/Master_DMA.csv', names=r_cols)

master = pd.read_csv('/home/hduser/Desktop/processWords/Master_DMA.csv',names=r_cols)

print adwords.describe()

print master.describe()

#merged = pd.concat([partial,master])

#print merged.describe()

merged_table =  pd.merge(adwords, master, on='City', how='inner')

merged_table.to_csv("/home/hduser/Desktop/processWords/joinTable.csv", encoding='utf-8')

print merged_table.describe()
