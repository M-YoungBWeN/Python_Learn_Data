"""
匿名函数lambda：没名的函数，只能使用一次
使用情况
1.函数的函数体只有一句且只有一个返回值时使用
2.列表取值
3.
"""


#
# 匿名函数 用于简化函数
# 正常函数
def calc(a, b):
    return a + b


print(calc(10, 20))

# 匿名函数 简化函数
s = lambda a, b: a + b  # s就是一个匿名函数
print('s的类型', type(s))
print(s(10, 20))  # 调用匿名函数

print('-' * 20)

#
# 匿名函数对列表取值
# 正常取值
lst = [10, 20, 30, 40, 50]
for i in range(len(lst)):
    print(lst[i])

print('-' * 20)
# 匿名函数 用于列表取值
for i in range(len(lst)):
    result = lambda x: x[i]
    print(result(lst))

print('-' * 20)
#
# 匿名函数 对列表排序
student_scores = [
    {'name': 'xx', 'score': 98},
    {'name': 'yy', 'score': 99},
    {'name': 'uu', 'score': 75},
    {'name': 'cc', 'score': 88},
    {'name': 'zz', 'score': 69}
]

student_scores.sort(key=lambda x: x.get('score'), reverse=True)
print(student_scores)
