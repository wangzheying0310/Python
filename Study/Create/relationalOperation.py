
# 布尔值 true 1 false 0

# > < >= <= == !=

a = int(input("输入我们球队的实力："))
b = int(input("输入b球队的实力："))
c = int(input("输入c球队的实力："))
d = int(input("输入d球队的实力："))

avsb = (a > b) * 3 + (a == b)
avsc = (a > c) * 3 + (a == b)
avsd = (a > d) * 3 + (a == b)

score = avsb + avsc + avsd

print("小足球赛可以得%d分"%(score))