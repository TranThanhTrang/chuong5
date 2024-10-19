# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:11:30 2024

@author: Administrator
"""

#Tạo một danh sách tự động các số chẵn nguyên và chia hết cho 5 từ 2018 đến 2828.
ds = [0] * ((2828-2018) // 2 + 1)
id = 0

for i in range (2018,2829):
    if i % 2 == 0 :
        ds[id]=i
        id +=1
        
# Tạo danh sách các số chia hết cho 9
chia_9 = [0] * (id)  # Khởi tạo danh sách với kích thước tối đa
id_9 = 0

for num in ds:
    if num != 0 and num % 9 == 0:  # Kiểm tra các số hợp lệ
        chia_9[id_9] = num
        id_9 += 1

# In các số thu được thành chuỗi, cách nhau bằng 1 tab
for i in range(id_9):
    if i == id_9 - 1:
        print(chia_9[i], end='')  # Không thêm tab sau số cuối
    else:
        print(chia_9[i], end='\t')  # Thêm tab giữa các số
        
        

        

