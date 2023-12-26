# -*- coding:utf-8 -*-
import os
import pandas as pd
# 获取文件夹下的所有CSV文件的路径
folder_path = 'D:/Goodo/AutoTesting/Python/test-zhang/Max_Model+Max_Battery'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# 遍历所有的CSV文件
for csv_file in csv_files:
    # 读取CSV文件内容
    df = pd.read_csv(os.path.join(folder_path, csv_file))

    # 查找包含"Time"文字的列
    result = df.applymap(lambda x: "Time" in str(x))

    # 如果找到了"Time"，打印出该CSV文件的名称以及"Time"所在行列
    if result.any().any():
        print(f'File: {csv_file}')
        for i in range(len(result)):
            for j in range(len(result.columns)):
                if result.iloc[i, j]:
                    print(f'Row: {i}, Column: {j}')
        # 将Time所在列的下一个单元格向下填充直到最后一行
        df.fillna(method='ffill', axis=0, inplace=True)

        # 在原CSV文件上进行修改保存，不生成新的文件
        # df.to_csv(os.path.join(folder_path, csv_file), index=False)
