# main 파일

import numpy as np
import pandas as pd
from pandas import DataFrame
import pandas_datareader as pdr
from datetime import datetime

import DataModify as Modify

q = 1

TotalLogRetNorm = pd.read_csv('./ResultData/TotalLogRetNorm.csv', index_col=0)
CrossCorr = TotalLogRetNorm.corr(method=Modify.crossCorr)
CrossCorr.to_csv("./ResultData/CrossCorrelation.csv")
MetricDist = Modify.metricdist(CrossCorr)
MetricDist.to_csv("./ResultData/MetricDistance.csv")
LinAutoCorr = Modify.linAutoCorr(TotalLogRetNorm)
LinAutoCorr.to_csv("./ResultData/LinearAutoCorrelation.csv")
NonLinAutoCorr = Modify.nonLinAutoCorr(TotalLogRetNorm, q)
NonLinAutoCorr.to_csv("./ResultData/NonLinearAutoCorrelation.csv")

# Data shuffle
TotalLogRetNorm_random=TotalLogRetNorm.sample(frac=1).reset_index(drop=True)
CrossCorr_random = TotalLogRetNorm_random.corr(method=Modify.crossCorr)
CrossCorr_random.to_csv("./ResultData/CrossCorrelation_random.csv")
MetricDist_random = Modify.metricdist(CrossCorr_random)
MetricDist_random.to_csv("./ResultData/MetricDistance_random.csv")
LinAutoCorr_random = Modify.linAutoCorr(TotalLogRetNorm_random)
LinAutoCorr_random.to_csv("./ResultData/LinearAutoCorrelation_random.csv")
NonLinAutoCorr_random = Modify.nonLinAutoCorr(TotalLogRetNorm, q)
NonLinAutoCorr_random.to_csv("./ResultData/NonLinearAutoCorrelation_random.csv")

print(LinAutoCorr);print(LinAutoCorr_random)