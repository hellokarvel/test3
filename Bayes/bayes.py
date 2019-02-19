#长恨人心不如水，等闲平地起波澜
#!/usr/bin/python
# -*- coding: <encoding name> -*-
from numpy import *
import operator
def loadDataSet(): #创建数据
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]# 1代表侮辱性文字
    return postingList,classVec

def createVocabList(dataSet):
    vocaSet = set([])
    for document in dataSet:
        vocaSet = vocaSet | set(document)
        # print('--------')
        # print(vocaSet)

    return list(vocaSet)



if __name__ == '__main__':
    a,b=loadDataSet()
    print(a)
    c=createVocabList(a)
    print(c)