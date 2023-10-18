def func(x):
    res = 0
    for i in range(x):
        res += i
    return res
print(func(4))


def print_nums(x):
    for i in range(x):
        print(i)
        return
print_nums(10)


def max(x, y):
    if x >=y:
        return x
    else:
        return y
print(max(4, 7))
z = max(8, 5)
print(z)

def shout(word):
    return word + "!"
speak = shout
output = speak("shout")
print(output)

def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))