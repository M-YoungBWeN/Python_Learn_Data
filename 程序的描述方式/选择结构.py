num = eval(input('输入一个数'))

if num == 2:
    print('True')

if num != 2:
    print('False')

print('-' * 20)

if num % 2:
    print(num, "是奇数")  # 2是偶数，2%2 = 0，if不执行
if not num % 2:
    print(num, '是偶数')

print('-' * 20)

x = input('输入字符串')
if x:
    print('字符串非空')
if not x:
    print('空字符串')

print('-' * 20)

# 使用if语句时，如果语句块中只有一句代码，可以将语句块直接写在冒号的后面
a = 10
b = 5
if a > b: max = a
print('max =', max)
