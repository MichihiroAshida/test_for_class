# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです。
"""
import numpy as np
from functools import reduce
from operator import add

a = [-1,4,9]
b = [1,1,1]
c = [-1,0,1]

a2 = list(map(lambda x: x*x , a))
b2 = list(map(lambda x: x*x , b))
c2 = list(map(lambda x: x*x , c))

a3 = reduce(add,a2)
b3 = reduce(add,b2)
c3 = reduce(add,c2)


sita=np.dot(a,b)/np.sqrt(a3*b3)
bou=np.dot(a,c)/np.sqrt(a3*c3)

print(sita*bou)

d=[1,1,2]
e=4
