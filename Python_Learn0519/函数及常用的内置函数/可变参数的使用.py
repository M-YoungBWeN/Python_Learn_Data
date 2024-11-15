"""
函数的可变参数：
1.个数可变的位置参数 *para
    放到元组中
2.个数可变的关键字参数 **para
    放到字典中
"""


#
# 个数可变的位置参数 *para
def fun(*para):  # para 是参数名
    print(type(para))  # para的类型是元组
    for item in para:
        print(item)


# 调用
fun(10, 20, 30)
fun()  # 没传参数
fun([10, 20, 30])  # 传入一个列表，实际上传的是一个参数
fun(*[10, 20, 30])  # 在列表前加* 对列表进行解包操作

print('-' * 20)


#
# 个数可变的关键字参数 **para
def fun2(**kwpara):
    print(type(kwpara))
    for key, values in kwpara.items():  # 要用items函数对kwpara字典取值
        print(key, '-->', values)


fun2(name='xx', age='20', height=178)
d = {'name': 'yy', 'age': 18, 'height': 178}
# fun2(d) ERROR 这样传的是一个字典结构的位置参数
fun2(**d)   # 用** 对字典d解包
