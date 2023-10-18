i = 0

while i * i < 1000:
    i += 1
    if i == 30:
        break

    print("i =" + str(i))
# print("i =" + i)报错
    print("i =" ,i)
    print("i * i = " + str(i * i))
else:
    print('while over!')