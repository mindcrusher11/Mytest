import pandas as pd

partial_dma = pd.ExcelFile("/home/hduser/Partial DMA.xlsx")

master_dma = pd.ExcelFile("/home/hduser/Master DMA.xlsx")

partial_dma.sheet_names

master_dma.sheet_names

dfPartial = partial_dma.parse("Sheet1")

dfPartial.head()

master_dma.sheet_names

dfMaster = master_dma.parse("Master Table")

dfMaster.head()

