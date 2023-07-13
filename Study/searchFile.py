import os
import shutil

# path 代表带搜索的目录路径，result 存储搜索到的文件路径列表
# 函数将path目录中的全部子目录和文件找到并保存至result
def search_dir(path,result):
    # 使用os中的listdir得到path下的目录和文件，保存到child_files
    child_files = os.listdir(path)
    # 遍历child_files
    for child in  child_files:
        # 通过join函数拼接子目录或文件的路径，存储到child
        child = os.path.join(path,child)
        # 将child保存至result
        result.append(child)
        # 如果child是子目录，调用search_dir继续递归
        if os.path.isdir(child):
            search_dir(child,result)