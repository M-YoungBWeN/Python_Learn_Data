"""
元组：不可变数据类型。可以获取和遍历
元组的定义：使用()定义

元组可以作为字典的键
"""

#
# 元组的创建
# 使用()创建
t = ('hello', [10, 20, 30], 666, 'python')
print(t)
# 使用tuple()创建
t2 = tuple('python')
print(t2)
t2 = tuple([10, 20, 30])
print(t2)

print('-' * 20)
#
# 元组也是序列，可以用序列的内置函数和方法
print('10是否存在：', (10 in t2))
print('10是否不存在：', (10 not in t2))
print('最大值：', max(t2))
print('最小值：', min(t2))
print('t2长度：', len(t2))
print('10的索引index：', t2.index(10))
print('10出现的次数count', t2.count(10))

print('-' * 20)
#
# 如果元组中只有一个元素，要加上,否则不会被设置为元组
t3 = (10)
print(type(t3))

t3 = (10,)
print(type(t3))

#
# 元组的删除
del t
del t2
del t3
