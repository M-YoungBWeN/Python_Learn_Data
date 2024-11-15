#
# 遍历for循环与while循环
for i in 'hello':
    print(i)

print('-' * 20)

s = 0
for i in range(1, 11):  # [1, 11)
    # range()是python的一个内置函数,用来创建一个整数序列(开始，结束不包含，步长)
    # print(i)
    if i % 2 == 0:
        print(i, '是偶数', sep='')
    s += i
print('s=', s, sep='')

print('-' * 20)

s2 = 0
i = 1
while i <= 10:
    s2 += i
    i += 1
else:
    print('s2=', s2, sep='')

#
# if...break 退出循环结构
# if...continue 跳过本次循环
print('-' * 20)
s3 = 0
i = 1
while i <= 10:
    if i % 2 == 1:
        i += 1
        continue
    s3 += i
    i += 1
else:
    print('s3=', s3, sep='')

#####
s4 = 0
for i in range(1, 11):
    if i % 2 == 1:
        i += 1
        continue
    s4 += i
    i += 1
print('s4=', s4, sep='')
