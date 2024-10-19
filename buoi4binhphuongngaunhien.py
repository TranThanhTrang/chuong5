# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:06:56 2024

@author: Administrator
"""

import random

# Số lượng phần tử ngẫu nhiên trong khoảng từ 18 đến 99
chonngaunhien = random.randint(18, 99)
print(chonngaunhien)

# Khởi tạo danh sách với các giá trị mặc định
dsrong = [0] * chonngaunhien

# Cập nhật từng phần tử của danh sách với bình phương của số thực ngẫu nhiên
for i in range(chonngaunhien):
    phantu = random.uniform(18, 99)
    dsrong[i] = phantu ** 2

# In ra danh sách
print("Danh sách các giá trị bình phương:")
print(dsrong)
