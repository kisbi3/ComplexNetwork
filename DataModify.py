''' 데이터 변형하는 함수를 모아두는 파일 '''
''' 상관관계 등 여러가지 구하는 함수들을 모아두는 파일'''

import numpy as np
import pandas as pd

'''
    logRet : Loagrithmic Return
    logRetNorm : Normalized Logarithmic Return
    linAutoCorr : Linear Auto-Correlation
    nonLinAutoCorr : NonLinear Auto-Correlation
    crossCorr : Cross-Correlation
    metricdist : metric distance
'''

def modify(RawData, Name):
    Modify = pd.DataFrame()
    LogRet = np.log(RawData.Close) - np.log(RawData.Close.shift(1))
    LogRet = LogRet.drop(LogRet.index[0])
    LogRetNorm = (LogRet-np.average(LogRet))/np.std(LogRet)
    Modify['Price'] = RawData.Close.drop(RawData.Close.index[0])
    Modify['LogReturn'] = LogRet
    Modify['LogReturnNorm'] = LogRetNorm
    Modify.to_csv(f"./ModifiedData/{Name}.csv")
    return LogRetNorm

def linAutoCorr(LogRetNorm):
    LogRetNorm_new = LogRetNorm.drop(LogRetNorm.index[0])
    LogRetNorm_old = LogRetNorm.shift(1).drop(LogRetNorm.shift(1).index[0])
    print(LogRetNorm_new*LogRetNorm_old)
    print( np.average(LogRetNorm_new)*np.average(LogRetNorm_old))
    return np.average(LogRetNorm_new*LogRetNorm_old) - np.average(LogRetNorm_new)*np.average(LogRetNorm_old)
    # return np.average(LogRetNorm*LogRetNorm.shift(1)) - np.average(LogRetNorm)*np.average(LogRetNorm.shift(1))

def nonLinAutoCorr(LogRetNorm, q):
    return np.average(np.abs(LogRetNorm*LogRetNorm.shift(1))**q) - np.average(np.abs(LogRetNorm)**q)*np.average(np.abs(LogRetNorm.shift(1))**q)

def crossCorr(i, j):
    return (np.average(i*j) - np.average(i)*np.average(j)) / (np.std(i)*np.std(j))

def metricdist(corr):
    return np.sqrt(2*(1-corr))