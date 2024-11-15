"""
通过下划线_可以控制属性或方法的访问权限
1.单下划线开头 受保护属性或方法
2.双下划线开头 私有属性或方法
3.首位双下划线 一般表示特殊的方法
"""


class Student():  # Student类后面的括号在没有继承或默认继承object的情况下可写可不写
    def __init__(self, name, age, gender):
        self._name = name  # 受保护属性，本类和子类可访问
        self.__age = age  # 私有属性，本类可访问。出了class的定义范围就不能用了
        self.gender = gender  # 普通属性，本类、子类和外部都可访问

    def _fun1(self):
        print('本类和子类可访问')

    def __fun2(self):
        print('本类可访问')

    def fun3(self):
        print('类内外和子类都可访问')

    def shou(self):
        self._fun1()
        self.__fun2()
        print(self._name, self.__age, self.gender)


# 创建一个学生对象
obj = Student('xx', 20, '男')
# 类的外部
obj.shou()

print('-'*20)

print(obj._name)  # 类和子类可访问
# print(obj.__age)  ERROR age 为类的私有属性
obj._fun1()
# obj.__fun2()  # ERROR 私有方法，本类可访问。出了class的定义范围就不能用了


print('-' * 20)
#
# 访问私有属性、方法（不推荐的方法）
# 推荐使用属性装饰器@property访问或修改私有属性
print(dir(obj))  # dir()函数在Python中是一个内置函数，用于返回当前作用域中所有变量、函数、类等的列表。
print(obj._Student__age)
obj._Student__fun2()
