"""
布尔值为False的情况如下
1.False 或者是None
2.数值中的0，包含0，0.0，虚数0
3.空序列,包含空字符串、空元组、空列表、空字典、空集合
4.自定义对象的实例，该对象的bool()方法返回False或len()方法返回0
"""
print(bool('字符串'))
print(bool(''))
print('---------------------')
my_bool = True
my_bool1 = 999
my_bool2 = 0
my_bool3 = 0.0
print(type(my_bool))
print(type(my_bool1))
print(bool(my_bool1), bool(my_bool2), bool(my_bool3))
