"""
三种遍历方式
1.for循环
2.for range()
3.for enumerate
"""
lst = ['hello', 'world', 'python', 'and', 'pyqt']
for i in lst:
    print(i)

for i in range(0, len(lst)):
    print(i, '-->', lst[i])
print('-' * 20)
for i, n in enumerate(lst):  # enumerate()返回序号和内容
    print(i, n)
print('-' * 20)
for i, n in enumerate(lst, start=1):  # 更改enumerate()序号起始位置
    # 可以直接写成enumerate(lst, 1)
    print(i, n)
