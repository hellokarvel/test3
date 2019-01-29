#长恨人心不如水，等闲平地起波澜
#!/usr/bin/python
# -*- coding: <encoding name> -*-
from numpy import *
import operator
def createDateSet():
      group=array([[1,1.1],[1,1],[0,0],[0,0.1]])
      labels = ['A','A','B','B']
      print('成功调用')
      return group,labels

def classify0(inX,dataSet,labels,k):
      dataSetSize = dataSet.shape[0]
 #读取第一维长度，即行数量
      diffMat=tile(inX,(dataSetSize,1))-dataSet
#tile将inX扩展为（行，列）的倍数。此句顺带减去训练样本
      sqDiffMat=diffMat **2
      sqDistances=sqDiffMat.sum(axis=1)
#.sum(),指定行或列相加，结果为1行,结果为array([3, 5])。
      distances=sqDistances**0.5
      sortedDistIndicies=distances.argsort()#从小到大，返回索引值.
      classCount={}#字典
      for i in range(k):
            voteIlabel=labels[sortedDistIndicies[i]]
            #对应上面，由小到大取出标签值
            classCount[voteIlabel]= classCount.get(voteIlabel,0)+1
            #查找对于标签的值。最后的value为最小的k个特征值
      sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
      #排序，按字典中的“值”排序，默认“Flase”为升序。此题为降序，找出现最多的标签
      return   sortedClassCount[0][0]#只输出第一项的key。第二个0是关键。

def file2matrix(filename):
      fr = open(filename)
      array0Lines = fr.readlines()    #依次读取每行
      numberOfLines = len(array0Lines)#返回对象（字符、列表、元组等）长度或项目个数
      returnMat =zeros((numberOfLines,3))#创建行*列矩阵
      classLabelVector=[] #列表
      index = 0
      for line in array0Lines:
            line=line.strip()# 方法用于移除字符串头尾指定的字符
            listFromLine = line.split('\t')#split() 通过指定分隔符对字符串进行切片
            returnMat[index,:]=listFromLine[0:3]#return的第index行放入前三个，注意*是三个
            if listFromLine[-1] == 'didntLike':#与原书有出入
                  classLabelVector.append(1)
            elif listFromLine[-1] == 'smallDoses':
                  classLabelVector.append(2)
            elif listFromLine[-1] == 'largeDoses':
                  classLabelVector.append(3)
            index +=1
      return returnMat,classLabelVector

def autoNorm(dataSet):
      minVals = dataSet.min(0)
      maxVals = dataSet.max(0)
      ranges  = maxVals-minVals
      normDataSet = zeros(shape(dataSet))#创建dataSet等行列矩阵
      m = dataSet.shape[0]
      normDataSet = dataSet - tile(minVals,(m,1))#数据- 一列
      normDataSet = normDataSet/tile(ranges,(m,1))#数据/范围
      return normDataSet, ranges, minVals

def datingClassTest():
      hoRatio = 0.1
      datingDataMat,datingLabels = file2matrix('datingTestSet.txt')
      normMat, ranges, minVals = autoNorm(datingDataMat)
      m = normMat.shape[0]#行代表数据的数量，乘0.1代表取10%数据
      numTestVecs = int(m*hoRatio)
      errorCount = 0.0
      for i in range(numTestVecs):
            classifierRestult = classify0(normMat[i,:],normMat[ \
                  numTestVecs:m,:],datingLabels[numTestVecs:m],3)
            print('the classifier came back with: %d,the real answer is:%d' %(classifierRestult,datingLabels[i]))
            if(classifierRestult != datingLabels[i]):errorCount +=1.0
      print('the total error rate is :%f' %(errorCount/float(numTestVecs)))

def classifyPerson(filename):
      resultList = ['not at all','in small doses ','in large doses']
      percentTats = float(input('percentage of time spent playing video games?'))
      ffmiles = float(input('frequent flier miles earned per year?'))
      iceCream = float(input('liters of ice cream consumed per years ?'))
      datingDataMat,datingLabels = file2matrix(filename)
      normMat, ranges, minVals = autoNorm(datingDataMat)
      inArr = array([ffmiles,percentTats,iceCream])
      classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
      print('You will probably like this peison:',resultList[classifierResult-1])

if __name__ == '__main__':#使文件既是函数，又是主函数
    #打开的文件名
    # filename = "datingTestSet.txt"
    # #打开并处理数据
    # datingDataMat, datingLabels = file2matrix(filename)
    # showdatas(datingDataMat, datingLabels)
      filename = 'datingTestSet.txt'
      classifyPerson(filename)
