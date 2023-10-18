import cmath

num = int(input("Please enter a number："))
num_sqrt = cmath.sqrt(num)
print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))