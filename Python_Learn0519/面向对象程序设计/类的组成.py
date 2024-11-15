"""
类：
1.类属性
2.实例属性
3.实例方法
4.静态方法
5.类方法

对象：类的实现
"""


#
#
class Student:
    school = 'YTU'  # 类属性：定义在类中 方法外的变量

    # 初始方法方法
    def __init__(self, name, age):  # name，age是方法的参数 是局部变量 作用于整个__init__方法
        self.name = name  # = 左侧是实例属性，右侧是局部变量。
        self.age = age

    # 实例方法   定义在类中的函数成为方法，自带一个self参数
    def show(self):
        print(f'姓名{self.name}，年龄{self.age}')

    # 静态方法  使用装饰器@staticmethod修饰的方法
    @staticmethod
    def sm():
        print('静态方法，无法使用实例属性和实例方法')

    # 类方法   使用装饰器@classmethod修饰的方法
    @classmethod
    def cm(cls):
        print('类方法，无法使用实例属性和实例方法')


#
# 对象
# 创建对象
stu = Student('xx', 20)  # __init__方法中传两个参数

# 实例属性 使用对象打点调用
print(stu.name, stu.age)

# 类属性 直接使用类打点调用
print(Student.school)

# 实例方法 使用对象打点调用
stu.show()

# 静态方法 使用类打点调用
Student.sm()

# 类方法 使用类打点调用
Student.cm()
