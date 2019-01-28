import operator
from numpy import *
import kNN
'''dict = {'Name': 1, 'Age': 7, 'Class': 4, 'Class2': 3}
a = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
print(a[0][1])'''


'''c='sh  adiao'
d= b.strip()
print(b)
print(d)
str = "72993	10.141740	1.320955	didntLike"
f=zeros((5,3))
e= str.split('\t')   #以 \t 为分隔符
      # 以空格为分隔符，包含 \n
f[0,:]=e[0:3]
print(f)'''
#print (str.split(' ', 1 )) # 以空格为分隔符，分隔成两
#以上实例输出结果：
#dict['Name']:  Zara
#dict['Age']:  7
#re, cla = kNN.file2matrix('a.txt')

mat1,lab1=kNN.file2matrix('a.txt')
print(mat1,lab1)