"""
列表：可变数据类型
列表的定义：使用[]定义
"""


# 使用[]创建
lst = ['hello', 'world', 202, 4]
print(lst)

# 使用list()创建
lst2 = list('hello')
print(lst2)
lst3 = list(range(1, 10, 2))
print(lst3)

print(lst + lst2 + lst3)
# 列表也是序列，序列的函数方法列表都可以用

#
# 列表的删除
del lst
del lst2
