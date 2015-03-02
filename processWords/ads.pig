Define CSVExcelStorage org.apache.pig.piggybank.storage.CSVExcelStorage;

adsData = LOAD 'hdfs://slave5:8020/user/hdfs/dma/AdWords_updated.csv' USING CSVExcelStorage(',', 'NO_MULTILINE', 'NOCHANGE') AS (City,Criteria,ID,State,DMA);

masterData = LOAD 'hdfs://slave5:8020/user/hdfs/dma/Master_DMA.csv' USING CSVExcelStorage(',', 'NO_MULTILINE', 'NOCHANGE') AS (City,State,ZipCode,StateAbr,Latitude,Longitude,DMARegion);

describe adsData;

describe masterData;

limitJoinedData = LIMIT adsData 10;

DUMP limitJoinedData;

joinedData = JOIN adsData BY (City,State) , masterData BY (City,State);

describe joinedData;

limitJoinedMasterData = LIMIT joinedData 10;

DUMP limitJoinedMasterData;

groupData = GROUP adsData BY (City,State) , masterData BY (City,State);

describe groupData;


