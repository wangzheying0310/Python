# 可以通过向打开函数应用第二个参数指定用于打开文件的模式。
# 发送“R”意味着在读取模式下打开，这是默认的。
# 发送“W”意味着写入模式，用于重写文件的内容。
# 发送“A”意味着追加模式，将新内容添加到文件的末尾。
# 在模式中添加“B”以二进制模式打开它，它用于非文本文件（如图像和声音文件）。

# file = open("newfile.txt", "w")
# file.write("写入字符串在文件里")
# file.close()
# file = open("newfile.txt", "r")
# print(file.read())
# file.close()

# file = open("newfile.txt", "r")
# print("初始化读写内容")
# print(file.read())
# print("完成")
# file.close()
#
# file = open("newfile.txt", "w")
# file.write("新的内容")
# file.close()
#
# file = open("newfile.txt", "r")
# print("写入新的内容")
# print(file.read())
# print("结束")
# file.close()

# write方法返回写入文件的字节数。
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
