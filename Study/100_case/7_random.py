# random.random() 返回一个介于 0.0 和 1.0 之间的随机小数
import random

random_number = random.random()
print(random_number)

# random.randint(a, b) 用于返回一个介于 a 和 b 之间的整数（包括 a 和 b）
# 生成 0 ~ 9 之间的随机数
print(random.randint(0, 1000))


# random.choice(sequence) 用于从序列中随机选择一个元素
list1 = [1, 2, 3, 4, 5]
random_element = random.choice(list1)
print(random_element)

# random.shuffle(sequence) 用于将序列中的元素进行随机排序
list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print(list1)