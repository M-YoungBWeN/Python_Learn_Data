import random
#
d = {item: random.randint(1, 100) for item in range(4)}
print(d)

# 用两个列表创建
lst1 = [1001, 1002, 1003]
lst2 = ['lego', 'python', 'pyqt']
d2 = {key: value for key, value in zip(lst1, lst2)}
print(d2)
