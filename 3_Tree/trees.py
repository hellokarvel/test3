#长恨人心不如水，等闲平地起波澜
#!/usr/bin/python
# -*- coding: <encoding name> -*-
from numpy import *
import operator
import math

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)#信息数量
    labelCounts ={}#字典
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts = 0
        labelCounts[currentLabel] +=1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -=prob *log(prob,2)
    return shannonEnt