''' 데이터 수집하는 파일 '''


import numpy as np
import pandas as pd
from pandas import DataFrame
import pandas_datareader as pdr
from datetime import datetime

import DataModify as Modify


IndicesPrice = {}
IndicesLogretNorm = {}


start = datetime(2000,1,1)
end = datetime(2021,12,31)

''' 미국 '''
# S&P 500
US = pdr.DataReader('^GSPC', 'yahoo', start, end)
US.to_csv("./RawData/US.csv")
USLogRetNorm = Modify.modify(US, 'US')
IndicesPrice["US"] = US.Close
IndicesLogretNorm["US"] = USLogRetNorm
print("US End")
''' 캐나다 '''
# S&P/TSX Composite index
Canada = pdr.DataReader('^GSPTSE', 'yahoo', start, end)
Canada.to_csv("./RawData/Canada.csv")
CanadaLogRetNorm = Modify.modify(Canada, 'Canada')
IndicesPrice["Canada"] = Canada.Close
IndicesLogretNorm["Canada"] = CanadaLogRetNorm
print("Canada End")

''' Western Europe '''
# DAX 독일
Germany = pdr.DataReader('^GDAXI', 'yahoo', start, end)
Germany.to_csv("./RawData/Germany.csv")
GermanyLogRetNorm = Modify.modify(Germany, 'Germany')
IndicesPrice["Germany"] = Germany.Close
IndicesLogretNorm["Germany"] = GermanyLogRetNorm
print("Germany End")
# AEX 네덜란드
Netherlands = pdr.DataReader('^AEX', 'yahoo', start, end)
Netherlands.to_csv("./RawData/Netherlands.csv")
NetherlandsLogRetNorm = Modify.modify(Netherlands, 'Netherlands')
IndicesPrice["Netherlands"] = Netherlands.Close
IndicesLogretNorm["Netherlands"] = NetherlandsLogRetNorm
print("Netherlands End")
# CAC 40 프랑스
France = pdr.DataReader('^FCHI', 'yahoo', start, end)
France.to_csv("./RawData/France.csv")
FranceLogRetNorm = Modify.modify(France, 'France')
IndicesPrice["France"] = France.Close
IndicesLogretNorm["France"] = FranceLogRetNorm
print("France End")
# IBEX 35 스페인
Spain = pdr.DataReader('^IBEX', 'yahoo', start, end)
Spain.to_csv("./RawData/Spain.csv")
SpainLogRetNorm = Modify.modify(Spain, 'Spain')
IndicesPrice["Spain"] = Spain.Close
IndicesLogretNorm["Spain"] = SpainLogRetNorm
print("Spain End")
# SMI PR 스위스
Switzerland = pdr.DataReader('^SSMI', 'yahoo', start, end)
Switzerland.to_csv("./RawData/Switzerland.csv")
SwitzerlandLogRetNorm = Modify.modify(Switzerland, 'Switzerland')
IndicesPrice["Switzerland"] = Switzerland.Close
IndicesLogretNorm["Switzerland"] = SwitzerlandLogRetNorm
print("Switzerland End")
# BEL 20 - 벨기에
Belgium = pdr.DataReader('^BFX', 'yahoo', start, end)
Belgium.to_csv("./RawData/Belgium.csv")
BelgiumLogRetNorm = Modify.modify(Belgium, 'Belgium')
IndicesPrice["Belgium"] = Belgium.Close
IndicesLogretNorm["Belgium"] = BelgiumLogRetNorm
print("Belgium End")

''' South America '''
# IBOVESPA - Brasil
Brasil = pdr.DataReader('^BVSP', 'yahoo', start, end)
Brasil.to_csv("./RawData/Brasil.csv")
BrasilLogRetNorm = Modify.modify(Brasil, 'Brasil')
IndicesPrice["Brasil"] = Brasil.Close
IndicesLogretNorm["Brasil"] = BrasilLogRetNorm
print("Brasil End")
# IPC MEXICO - Mexico
Mexico = pdr.DataReader('^MXX', 'yahoo', start, end)
Mexico.to_csv("./RawData/Mexico.csv")
MexicoLogRetNorm = Modify.modify(Mexico, 'Mexico')
IndicesPrice["Mexico"] = Mexico.Close
IndicesLogretNorm["Mexico"] = MexicoLogRetNorm
print("Mexico End")
# MERVAL - Argentina
Argentina = pdr.DataReader('^MERV', 'yahoo', start, end)
Argentina.to_csv("./RawData/Argentina.csv")
ArgentinaLogRetNorm = Modify.modify(Argentina, 'Argentina')
IndicesPrice["Argentina"] = Argentina.Close
IndicesLogretNorm["Argentina"] = ArgentinaLogRetNorm
print("Argentina End")


''' Africa/Middle east '''
# TA-125 - Israel
Israel = pdr.DataReader('^TA125.TA', 'yahoo', start, end)
Israel.to_csv("./RawData/Israel.csv")
IsraelLogRetNorm = Modify.modify(Israel, 'Israel')
IndicesPrice["Israel"] = Israel.Close
IndicesLogretNorm["Israel"] = IsraelLogRetNorm
print("Israel End")

''' ASIA/PACIFIC '''
# Australia All Ordinaries - Australia
Australia = pdr.DataReader('^AORD', 'yahoo', start, end)
Australia.to_csv("./RawData/Australia.csv")
AustraliaLogRetNorm = Modify.modify(Australia, 'Australia')
IndicesPrice["Australia"] = Australia.Close
IndicesLogretNorm["Australia"] = AustraliaLogRetNorm
print("Australia End")
# Jakarta Composite Index - Indonesia
Indonesia = pdr.DataReader('^JKSE', 'yahoo', start, end)
Indonesia.to_csv("./RawData/Indonesia.csv")
IndonesiaLogRetNorm = Modify.modify(Indonesia, 'Indonesia')
IndicesPrice["Indonesia"] = Indonesia.Close
IndicesLogretNorm["Indonesia"] = IndonesiaLogRetNorm
print("Indonesia End")
# Hang Seng - Hong Kong
HongKong = pdr.DataReader('^HSI', 'yahoo', start, end)
HongKong.to_csv("./RawData/HongKong.csv")
HongKongLogRetNorm = Modify.modify(HongKong, 'HongKong')
IndicesPrice["HongKong"] = HongKong.Close
IndicesLogretNorm["HongKong"] = HongKongLogRetNorm
print("HongKong End")
# KOSPI - Republic of Korea
Korea = pdr.DataReader('^KS11', 'yahoo', start, end)
Korea.to_csv("./RawData/Korea.csv")
KoreaLogRetNorm = Modify.modify(Korea, 'Korea')
IndicesPrice["Korea"] = Korea.Close
IndicesLogretNorm["Korea"] = KoreaLogRetNorm
print("Korea End")
# NIKKEI 225 - Japan
Japan = pdr.DataReader('^N225', 'yahoo', start, end)
Japan.to_csv("./RawData/Japan.csv")
JapanLogRetNorm = Modify.modify(Japan, 'Japan')
IndicesPrice["Japan"] = Japan.Close
IndicesLogretNorm["Japan"] = JapanLogRetNorm
print("Japan End")
# SENSEX - India
India = pdr.DataReader('^BSESN', 'yahoo', start, end)
India.to_csv("./RawData/India.csv")
IndiaLogRetNorm = Modify.modify(India, 'India')
IndicesPrice["India"] = India.Close
IndicesLogretNorm["India"] = IndiaLogRetNorm
print("India End")
# Shanghai Composite - China
China = pdr.DataReader('000001.SS', 'yahoo', start, end)
China.to_csv("./RawData/China.csv")
ChinaLogRetNorm = Modify.modify(China, 'China')
IndicesPrice["China"] = China.Close
IndicesLogretNorm["China"] = ChinaLogRetNorm
print("China End")
# TSEC weighted index - Taiwan
Taiwan = pdr.DataReader('^TWII', 'yahoo', start, end)
Taiwan.to_csv("./RawData/Taiwan.csv")
TaiwanLogRetNorm = Modify.modify(Taiwan, 'Taiwan')
IndicesPrice["Taiwan"] = Taiwan.Close
IndicesLogretNorm["Taiwan"] = TaiwanLogRetNorm
print("Taiwan End")

# NA 개수에 따라서 어떻게 할 지 정하는 threshold.
# 0.7 => 70퍼 이상이 숫자인 경우 Ok
nathreshold = round(len(IndicesPrice)*0.7)

TotalPrice = pd.DataFrame()
for name, index in IndicesPrice.items():
    TotalPrice = pd.concat([TotalPrice, index], axis=1)
    TotalPrice.rename(columns={'Close':name}, inplace=True)
TotalLogRetNorm = pd.DataFrame()
for name, index in IndicesLogretNorm.items():
    TotalLogRetNorm = pd.concat([TotalLogRetNorm, index], axis=1)
    TotalLogRetNorm.rename(columns={'Close':name}, inplace=True)

TotalPrice = TotalPrice.dropna(axis=0, thresh=nathreshold)
TotalPrice = TotalPrice.fillna(method='ffill')
TotalPrice = TotalPrice.drop(TotalPrice.index[0])
TotalPrice.index.name="Date"
TotalPrice['date'].TotalPrice.strftime('%Y-%m-%d')
TotalLogRetNorm = TotalLogRetNorm.dropna(axis=0, thresh=nathreshold)
TotalLogRetNorm = TotalLogRetNorm.fillna(method='ffill')
TotalLogRetNorm = TotalLogRetNorm.drop(TotalLogRetNorm.index[0])
TotalLogRetNorm.index.name="Date"
print(TotalPrice)
print(TotalLogRetNorm)

TotalPrice.to_csv(f"./ResultData/TotalPrice.csv")
TotalLogRetNorm.to_csv(f"./ResultData/TotalLogRetNorm.csv")