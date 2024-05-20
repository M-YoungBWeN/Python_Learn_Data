#
# 整数的表示形式
num1 = 64
num2 = 0b1000000
num3 = 0o100
num4 = 0x40

print(num1)
print(num2)
print(num3)
print(num4)

#
# 浮点数
num_f1 = 2.0
num_f2 = 2.0e1  # 科学计数法
num_f3 = 2e1
print(num_f1, type(num_f1))
print(num_f2, type(num_f2))
print(num_f3, type(num_f3))

print(0.1 + 0.2)
print(round(0.155 + 0.3, 2))  # 保留一位小数，五舍六入
print(round(3.1415926, 4))  # 保留四位小数，五舍六入

#
# 虚数
num_x = 123 + 456j
print('实部:', num_x.real, sep='')
print('虚部:', num_x.imag, sep='')
