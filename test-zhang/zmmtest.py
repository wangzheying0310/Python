import subprocess
import os
import pandas as pd

# 指定文件夹路径
folder_path = 'D:/Program Files/WeChat Files/WeChat Files/wxid_2wl7xwb84f0k22/FileStorage/File/2023-12/固定无功/Max_Model+Max_Battery'

# 遍历文件夹下的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否为CSV文件
    if filename.endswith('.csv'):
        # 读取CSV文件
        df = pd.read_csv(os.path.join(folder_path, filename))
        print(df)
        # 在这里处理数据...
        # 调用JavaScript文件并传递CSV文件路径作为参数
        subprocess.run(["node", "test.js", folder_path])


