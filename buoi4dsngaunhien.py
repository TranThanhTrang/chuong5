# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:12:06 2024

@author: Administrator
"""
#Viết chương trình có thể tạo danh sách:Số lượng các phần tử được chọn ngẫu nhiên từ 20 đến 30.


import random
chonngaunhien = random.randint(20, 30)
print(chonngaunhien)

# Khởi tạo danh sách với các giá trị mặc định là 0
dsrong = [0] * chonngaunhien

# Cập nhật từng phần tử của danh sách
for i in range(chonngaunhien):
    dsrong[i] = random.randint(1, 100)

print(dsrong)
