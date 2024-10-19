# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:02:15 2024

@author: Administrator
"""

# Khởi tạo biến để kiểm tra
value = None

# Sử dụng vòng lặp while để kiểm tra giá trị nhập vào
while value is None or not (-89.9 <= value <= 88.8):
    # Nhập giá trị từ người dùng
    n = input("Nhập một số trong khoảng [-89.9; 88.8]: ")

    # Kiểm tra xem giá trị có phải là số không
    if n.strip() and n.replace('-', '', 1).isdigit():
        value = int(n)  # Chuyển đổi giá trị thành số nguyên
    else:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số nguyên.")

# Kiểm tra điều kiện và in kết quả
if -89.9 <= value <= 88.8:
    print(f"Giá trị nhập vào hợp lệ: {value}")