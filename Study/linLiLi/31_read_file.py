# f = open("./data.txt", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()

# with open("./data.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)

# with open("./data.txt", "r", encoding="utf-8") as f:
#     print(f.readline())
#     print(f.readline())


with open("./data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)