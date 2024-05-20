s = '3.14+3'
print(s, type(s))
x = eval(s)
print(x, type(x))
print(round(x, 2))

#
# 与input搭配使用甚妙
age = eval(input('请输入年龄'))
height = eval(input('请输入身高'))
print(age, type(age))
print(height, type(height))
