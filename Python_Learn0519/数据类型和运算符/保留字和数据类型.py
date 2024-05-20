#
# 查看保留字
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))

"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

35个
"""

#
# 查询数据类型
my_num = 2
my_title = '666'

print(type(my_num), type(my_title))

#
# 允许多个变量指向同一个值
num1 = num2 = 2
print(id(num1))  # id()查看内存地址
print(id(num2))
