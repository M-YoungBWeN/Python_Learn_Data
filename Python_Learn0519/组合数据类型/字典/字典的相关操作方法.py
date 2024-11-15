d = {1001: '乐高', 1002: '模客', 1003: '潘洛斯'}
print(d)

#
# 向字典中添加元素
d[1004] = '乐集'
print(d)

#
# 获取字典元素的键
keys = d.keys()  # 获得的是一个对象dict_keys([1001, 1002, 1003, 1004])
print(keys)
print(list(keys))  # 可以用列表取出对象存的键
print(tuple(keys))  # 可以用元组取出对象存的键

print('-' * 20)
#
# 获取字典元素的值
values = d.values()
print(values)
print(list(values))  # 可以用列表取出对象存的值
print(tuple(values))  # 可以用元组取出对象存的值

print('-' * 20)
#
# 将字典的数据以key-value的形式展现
lst = list(d.items())  # 以列表的形式展现
print('以列表的形式展现', lst)
t = tuple(d.items())  # 以元组的形式展现
print('以元组的形式展现', t)

d2 = dict(lst)
print('把列表展现变回以字典的形式', d2)

print('-' * 20)
#
# 字典元素的删除
# 使用pop()函数
print(d.pop(1001))  # 会先取值，再删除
print(d)

print(d.pop(1008, '不存在'))  # 与get函数一样，pop函数也可以加一个默认值

# 随机删除
print(d.popitem())
print(d)

# 清空字典所有元素
d.clear()
print(d)
