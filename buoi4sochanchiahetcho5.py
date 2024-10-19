# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:47:30 2024

@author: Administrator
"""

ds = [0] * ((2828-2018) // 2 + 1)
id=0
for i in range (2018,2829):
    if i % 2 == 0 and i % 5 == 0 : 
        ds[id]=i
        id +=1
for i in range(id):
    print(ds[i], end='\t')
    
    
    