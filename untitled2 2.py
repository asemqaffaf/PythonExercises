#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:25:34 2019

@author: asemqaffaf
"""

import pandas as pd
import numpy as np
# 1
data = np.array([2, 4, 6, 8, 10])
print(arr)
# 2
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
d2 = pd.Series(d1)
print(d2)
# 3
data2 = [20, 10, 150, 110, 100, 50]
d2 = pd.Series(data2)
d2.plot(kind="bar")
# 4
data4= {
'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
data5 = pd.DataFrame(data4)
print(data5)
# 5

from pandas import DataFrame

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
Data2 = {'Names': [968, 155, 77, 578, 973]}
df = DataFrame(Data2,columns=['Names'],index =names )

df.plot.pie(y='Names',figsize=(5, 5),autopct='%1.1f%%', startangle=90)
# 6

df = pd.DataFrame(np.random.randn(8,4),index=dates,columns=list('PQRS'))
df = pd.read_csv('myDataFrame.csv',sep='\t',index_col=0)

# 7
dates = pd.date_range('20000101',periods=4)
df.random.randn(4,2)
print(dates)
print()