import random

#
#
# 生成一维列表
lst = [item for item in range(0, 11)]
print(lst)

lst = [item * item for item in range(0, 11)]
print(lst)

# 生成随机的列表
# random可以生成随机数
lst = [random.randint(1, 100) for _ in range(0, 11)]
print(lst)

# 从列表筛选复合条件的元素组成新的列表
lst = [i for i in range(0, 11) if i % 2 == 0]
print(lst)

print('-' * 20)
#
#
# 二维列表的遍历和生成
lss = [
    ['城市', '同比', '环比'],
    ['北京', '102', '104'],
    ['上海', '105', '106'],
    ['广州', '107', '108']
]
print(lss)

# 遍历二维列表
for row in lss: # 行
    for i in row:
        print(i, end='\t')
    print()  # 换行

# 生成二维列表(四行五列)
lss2 = [[j for j in range(5)] for row in range(4)]
for row in lss2:
    for i in row:
        print(i, end='\t')
    print()  # 换行
