#-*- coding:utf-8 -*-
__author__ = 'dengkun'


from numpy import *
arr=random.rand(4,4)
print(arr)
randMat=mat(arr)
print(randMat)
print("求逆：")
print(randMat.I)