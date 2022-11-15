# main 파일

import numpy as np
import pandas as pd
from pandas import DataFrame
import pandas_datareader as pdr
from datetime import datetime

import DataModify as Modify

TotalLogRetNorm = pd.read_csv('./TotalLogRetNorm.csv', index_col=0)
CrossCorr = TotalLogRetNorm.corr(method=Modify.crossCorr)
CrossCorr.to_csv("./CrossCorrelation.csv")
MetricDist = Modify.metricdist(CrossCorr)
MetricDist.to_csv("./MetricDistance.csv")
LinAutoCorr = Modify.linAutoCorr(TotalLogRetNorm)
print(LinAutoCorr)
LinAutoCorr.to_csv("./LinearAutoCorrelation.csv")
