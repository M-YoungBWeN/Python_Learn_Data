"""
元组的生成式结果是生成器对象，需要转化才能看到内容
生成器对象： <generator object <genexpr> at 0x0000020C412FA260>
"""
#
# 生成器对象的生成
t = (i for i in range(1, 11))
print(t)  # 输出的是一个生成器对象

# 生成器对象可以用__next__方法遍历
# 用__next__就把生成器对象的元素拿出开了
print(t.__next__())

#
# 元组对象的生成：把生成器对象转化为元组对象
t = tuple(t)  # 把这个生成器对象转化为元组
print(t)

# 元组的遍历
for i in t:
    print(i, ' ', end='')


