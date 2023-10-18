gpa_dict = {"小明":3.251,"小张":3.121,"小王":9.032,"小吉":3.111,}
for name,gpa in gpa_dict.items():
    print("{0}你好，你当前的绩点为:{1:.2f}".format(name,gpa))
    print(f"{name}你好，你当前的绩点为：{gpa:.2f}")