#
# 没有返回值的函数
def calc(a, b):
    print(a + b)


calc(10, 20)
print(calc(10, 20))  # None 没有返回值

print('-' * 20)


#
# 增加返回值
def calc2(a, b):
    return a + b


print(calc2(1, 2))
print(calc2(calc2(1, 2), 3))  # 1+2+3

print('-' * 20)


#
# 多个返回值
def get_num(num):
    s = 0  # 累加和
    odd_sum = 0  # 奇数累加和
    even_sum = 0  # 偶数累加和
    for i in range(1, num + 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
        s += i
    return odd_sum, even_sum, s


print(get_num(10), type(get_num(10)))
ax, bx, cx = get_num(10)  # 对函数多个返回解包
print('奇数和', ax, '偶数和', bx, '累加和', cx)
