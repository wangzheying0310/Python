# -*- coding: utf-8 -*-

import os

import pywintypes
import win32com.client

import win32com.client


def execute_osts_file(osts_file_path, folder_path):
    # 打开OSTS文件
    osts_app = win32com.client.Dispatch("Office.Application")
    osts_app.Open(osts_file_path)

    # 获取指定文件夹下的所有文件
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".osts"):
                file_list.append(os.path.join(root, file))

    # 遍历文件列表，执行每个OSTS文件
    for file_path in file_list:
        # 在此处添加你的代码，以执行OSTS文件并获取修改数据明细
        # 例如：result = osts_app.Execute(file_path)

        # 打印修改成功日志及修改数据明细
        print(f"成功执行OSTS文件：{file_path}")
        # print(f"修改数据明细：{result}")

    # 关闭OSTS应用程序
    osts_app.Close()


if __name__ == "__main__":
    osts_file_path = "D:/Program Files/WeChat Files/WeChat Files/wxid_2wl7xwb84f0k22/FileStorage/File/2023-12/固定无功/11_固定无功[!系数手改+重启运行03脚本].osts"  # 替换为你的OSTS文件路径
    folder_path = "D:/Program Files/WeChat Files/WeChat Files/wxid_2wl7xwb84f0k22/FileStorage/File/2023-12/固定无功/Max_Model+Max_Battery"  # 替换为你要处理的文件夹路径
    execute_osts_file(osts_file_path, folder_path)
