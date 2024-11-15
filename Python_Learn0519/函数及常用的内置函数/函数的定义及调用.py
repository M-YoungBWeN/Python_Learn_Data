"""
函数：函数名称、函数参数、实现功能的函数体
函数传参：位置传参、关键字传参、默认值传参

"""


#
# 没有写return的简单函数。把1到num累加起来
def get_sum(num):
    s = 0
    for i in range(1, num + 1):
        s += i
    print(f'1到{num}的累加和为{s}')  # 字符串前加f 表示可以在字符串里加入参数（不信可以删掉f看看输出啥）


get_sum(10)
get_sum(100)
get_sum(1000)

print('-' * 20)


#
# 简单函数
def happy_birthday(name, age):
    print('祝' + name + '生日快乐')
    print(str(age) + '岁生日快乐')  # 只有字符串之间才可以用+连接，用str()函数转为字符串再连接


happy_birthday('自己', 20)  # 位置传参：传参的类型和顺序要与函数定义时相同
happy_birthday(age=20, name='阿银')  # 关键字传参：顺序和位置不重要，注意类型就行。关键字要与函数原本的一致
happy_birthday('祖国', age=75)  # 混合使用的规则：位置参数在前，关键字参数在后


#
# 有默认值的简单函数

def happy_birthday2(age, name='None'):  # 默认传参：当位置参数和默认值参数同时存在时，位置参数必须放在默认值参数前面
    print('祝' + name + '生日快乐')
    print(str(age) + '岁生日快乐')  # 只有字符串之间才可以用+连接，用str()函数转为字符串再连接


happy_birthday2(age=0)  # 关键字传参
