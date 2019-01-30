#长恨人心不如水，等闲平地起波澜
#!/usr/bin/python
# -*- coding: <encoding name> -*-
from numpy import *
import operator
import math
from math import log

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)#信息数量
    labelCounts ={}#字典
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -=prob * log(prob, 2)
    return shannonEnt

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[0:axis]
            reducedFeatVec.extend(featVec[axis+1:])#和上一语句一起使用，去掉axis特征
            retDataSet.append(reducedFeatVec)
    return retDataSet



if __name__ == '__main__':#使文件既是函数，又是主函数
    #打开的文件名
    # filename = "datingTestSet.txt"
    # #打开并处理数据
    # datingDataMat, datingLabels = file2matrix(filename)
    # showdatas(datingDataMat, datingLabels)
    a,b =createDataSet()
    print(a)
    c=calcShannonEnt(a)
    print(c)
    print(splitDataSet(a,1,1))
    print(splitDataSet(a, 0, 1))