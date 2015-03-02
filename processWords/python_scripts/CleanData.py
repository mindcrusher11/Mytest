import csv
import pandas as pd

trainData = csv.reader(open("/home/hdfs/TrainData.csv","rb"))

for row in trainData:
	print row['name']

pd.

for tweet in tweepy.Cursor(api.search,
                           q="google",
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en",place="Birmingham, AL").items(10):
    print tweet.created_at,tweet

SELECT 
  * 
FROM 
  public.logging_event, 
  public.games, 
  public.teams;

copy <table_name> from 's3://<bucket_name>/<object_prefix>'
credentials 'aws_access_key_id=<access-key-id>;aws_secret_access_key=<secret-access-key>';

CREATE TABLE largecap("Ticker" character varying(68),"Short Name" character varying(68),"Market Cap" numeric,"P/E" numeric,"Total Return YTD" numeric,"Revenue T12M" numeric,"PX_TO_BOOK_RATIO" numeric)

CREATE TABLE largecap("Ticker" character varying(70),"Short Name" character varying(70),"Market Cap" numeric, "P/E" numeric,"Total Return YTD" numeric,"Revenue T12M" numeric,"PX_TO_BOOK_RATIO" numeric)

COPY largecap("Ticker","Short Name","Market Cap", "P/E","Total Return YTD" ,"Revenue T12M" ,"PX_TO_BOOK_RATIO")
FROM '/home/hduser/Desktop/processWords/stock_large_cap.csv'
WITH DELIMITER ','
CSV HEADER

COPY largecap("Ticker","Short Name","Market Cap", "P/E","Total Return YTD" ,"Revenue T12M" ,"PX_TO_BOOK_RATIO")
FROM 'https://s3-us-west-2.amazonaws.com/stadeaa-blobs/stock_large_cap.csv'
WITH DELIMITER ','
CSV HEADER credentials 'aws_access_key_id=AKIAIGNBY4GBJ7WG2PHQ';
	
This is a private link https://s3-us-west-2.amazonaws.com/stadeaa-blobs/stock_large_cap.csv

AKIAIGNBY4GBJ7WG2PHQ
