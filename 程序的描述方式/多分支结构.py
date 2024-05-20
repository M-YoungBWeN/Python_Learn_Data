score = eval(input('输入成绩'))
if score > 100 or score < 0:
    print('ERROR')
elif 101 > score > 89:
    print('A')
elif 90 > score > 59:
    print('B')
else:
    print('C')

#
# 嵌套结构
