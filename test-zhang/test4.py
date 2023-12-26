#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'mayi'
#
# import csv
#
# # 读
# with open("D:/Goodo/AutoTesting/Python/test-zhang/Max_Model+Max_Battery/PC-Max_Model+Max_Battery-Q=max-P=09@.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     rows = [row[2] for row in reader]
#
# print(rows)

# 导入os和pandas库
import os
import pandas as pd
import openpyxl

# 定义文件夹路径
folder_path = 'D:/Goodo/AutoTesting/Python/test-zhang/Max_Model+Max_Battery'

# 获取文件夹下的所有文件名
file_names = os.listdir(folder_path)

# 遍历所有文件名
for file_name in file_names:
    # 判断文件是否为CSV文件
    if file_name.endswith('.csv'):
        # 读取CSV文件
        df = pd.read_csv(os.path.join(folder_path, file_name))
        # 将CSV文件转换成.xlsx格式并保存
        df.to_excel(os.path.join(folder_path, file_name.replace('.csv', '.xlsx')), index=False)

