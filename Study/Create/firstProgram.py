# num_1 = input("请输入第一个数：")
# num_2 = input("请输入第二个数：")
# print(num_1 + num_2)

a = 20
print(type(a))
print('----二进制----')
b = 0b11
print(b)

e = int('11',base= 2)
print(e)
print('----八进制----')
c = 0o11
print(c)
print('----十六进制----')
d = 0x11
print(d)

print("=" * 30)
print("|"+" "*28+"|")
print("|"+" "* 7 +"I Love Python!"+" "* 7+"|")
print("|"+" "*28+"|")
print("=" * 30)

f = 13
g = 5

print(f / g)
print(f % g)
print(f // g)
print(f + g)
print(f - g)
print(f * g)
print(f ** g)

print(12 >=8)
print(12<=8)
print (10<= 12 <=15)
print(12 >=10<=15)
print(6<10 >8)
print("abc" == "abc")
print("abc" !="abe")
print("abc" >"abc")
print ("abc" >="abe")
print ("abc"<"abc")
print("abc"<="abc")
print ("abc"<= "abd")

h = 5 > 4 and 2
print(h)

h = 6 > 5 or 3
print(h)

h = 0x11
print("%o" %h)

h = 3 and 4
i = h ** 2
print(i)

a = 13
b = a/5 +a//5 +a % 5
print(b)
