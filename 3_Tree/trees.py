#长恨人心不如水，等闲平地起波澜
#!/usr/bin/python
# -*- coding: <encoding name> -*-
from numpy import *
import operator
import math
from math import log

def calcShannonEnt(dataSet):#香农商
    numEntries = len(dataSet)#信息数量
    labelCounts ={}#字典
    for featVec in dataSet:
        currentLabel = featVec[-1]#最后一项
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries#标签数量/总数
        shannonEnt -=prob * log(prob, 2)
    return shannonEnt
def createDataSet():#创造数据
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels

def splitDataSet(dataSet, axis, value):#按照特征划分数据集
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[0:axis]
            reducedFeatVec.extend(featVec[axis+1:])#和上一语句一起使用，去掉axis特征
            retDataSet.append(reducedFeatVec)
    return retDataSet
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0])-1 #数据列表的第一个列表
    baseEntropy = calcShannonEnt(dataSet)#Entropy 熵
    bestInfoGain = 0.0;bestFeature=-1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)#一列中的结果
        newEntropy = 0
        for value in uniqueVals:#一个for循环完 计算一个特征的信息熵
            subDataSet = splitDataSet(dataSet,i,value)#减去特征，只有符合value的值被选出
            prob = len(subDataSet)/float(len(dataSet))#所以为（符合value）数量/总数
            newEntropy += prob*calcShannonEnt(subDataSet)#概率*最后一列香农熵，局部
            infoGain = baseEntropy - newEntropy
            if(infoGain>bestInfoGain):
                bestInfoGain = infoGain
                bestFeature = i
    return bestFeature
def majorityCnt(classList):#若无法直接得到，采用投票法
    classCount = {}
    for vote in classCount:
        if vote not in classCount.keys():classCount[vote] = 0
        classCount[vote] +=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=Ture)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]  #获取dataSet的第i个所有特征
    if classList.count(classList[0])==len(classList):  #标签和长度相同
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])#删除变量
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree



if __name__ == '__main__':#使文件既是函数，又是主函数
    #打开的文件名
    # filename = "datingTestSet.txt"
    # #打开并处理数据
    # datingDataMat, datingLabels = file2matrix(filename)
    # showdatas(datingDataMat, datingLabels)
    a,b = createDataSet()
    myTree = createTree(a,b)
    print(myTree)