"""
内置函数：不需要前缀就可以使用的函数
类型转换函数、数学函数、迭代器函数、其他函数
"""

#
# 类型转换函数
# bool()
print('非空字符串的布尔值:', bool('hello'))
print('空字符串的布尔值:', bool(''))  # 空字符
print('空列表的布尔值:', bool([]))
print('空列表的布尔值:', bool(list()))
print('空元组的布尔值:', bool(()))
print('空元组的布尔值:', bool(tuple()))
print('空集合的布尔值:', bool(set()))
print('空字典的布尔值:', bool({}))
print('空字典的布尔值:', bool(dict()))
print('-' * 20)
# str()
# int()
# float()
# list() 列表
# tuple() 元组
# set() 集合

#
# 数学函数
# abs(x) x的绝对值
# divmod(x,y) x与y的商和余数
print(divmod(14, 3))
# max()
# min()
# sum(iter) 可迭代对象求和(如列表)
print(sum([10, 20, 30, 40, 50, 6]))
# pow(x,y) x的y次幂
print(pow(2, 10))
# round(x,d) 对x保留d位小数，四舍五入？
print('round只有一个参数，四舍五入保留整数：', round(3.9555611))
print('保留两位小数：', round(3.14159, 2))
print('对个位四舍五入：', round(314.15926, -1))
print('对十位四舍五入：', round(314.15926, -2))
print('-' * 20)

#
# 迭代器函数
# sorted()
# reversed() 反向 返回迭代器对象
lst = [66, 654, 99, 2, 999, 1]
lst_reversed = reversed(lst)
print(type(lst_reversed))
print(list(lst_reversed))
# zip() 组合 返回迭代器对象
x = [12, 23, 6, 49, 65]
y = ['a', 'b', 'c', 'd']
lst_zip = zip(x, y)
# print(type(lst_zip))
# print(list(lst_zip))
# enumerate() 生成索引 返回迭代器对象
lst_enumerate = enumerate(x, start=1)
print(type(lst_enumerate))
print(list(lst_enumerate))
# all() 返回布尔值，有False则返回False
# any() 返回布尔值，有True则返回True
# next() 遍历出来后就取出来了
print('遍历值', next(lst_zip))
print('遍历值', next(lst_zip))
print('遍历值', next(lst_zip))
print(list(lst_zip))  # 遍历结束后还剩一个


# filter(function, iter)
def fun(num):
    return num % 2 == 1  # 返回奇数


obj = filter(fun, range(10))
print(type(obj), list(obj))


# map(function, iter)
def upper(x):
    return x.upper()


lst2 = ['hello', 'python']
obj2 = map(upper, lst2)
print(type(obj2), list(obj2))
print('-' * 20)

#
# 其他函数
# format(value,format_spec) 将value以format spec格式进行显示
print(format(3.14, '20'))  # 数值型默认右对齐
print(format('hello''20'))  # 字符串默认左对齐
print(format('hello', '*<20'))  # <左对齐，*表示的填充符，20表示的是显示的宽度
print(format('hello', '*>20'))
print(format('hello', '*^20'))

print(format(3.1415926, '.2f'))  # 3.14
print(format(20, 'b'))
print(format(20, 'o'))
print(format(20, 'x'))
print(format(20, 'X'))
print('-' * 20)

# len(s) 获取s的长度或s元素的个数
# id(obj) 获取对象的内存地址
# type(x) 获取x的数据类型
# eval(s) 执s这个字符串所表示的Python代码--去除''
