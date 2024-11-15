"""
函数内部没有global声明的变量是局部变量
直接在外面定义的变量是全局变量
全局变量与局部变量冲突时，局部变量优先于全局变量
"""


def calc(x, y):
    global s
    s = 300
    return s + x + y


print(calc(10, 20))
print(s)
