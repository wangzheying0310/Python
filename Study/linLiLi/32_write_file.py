# 任务1：在poem.txt文件中写入以下内容
# 我欲乘风归去，
# 又恐琼楼玉宇，
# 高处不胜寒，

# 任务2：在poem.txt文件结尾处，添加一下两句
# 起舞弄清影。
# 何似在人间

with open("./poem.txt", "w", encoding="utf-8") as f:
    f.write("我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒，")

with open("./poem.txt", "a", encoding="utf-8") as f:
    f.write("\n起舞弄清影，\n何似在人间，\n")
