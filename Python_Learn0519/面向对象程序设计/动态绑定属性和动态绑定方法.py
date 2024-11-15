"""
动态绑定属性和动态绑定方法
"""


class Student:
    school = 'YTU'  # 类属性

    # 初始方法方法
    def __init__(self, name, age):  # name，age是方法的参数 是局部变量 作用于整个__init__方法
        self.name = name  # = 左侧是实例属性，右侧是局部变量。
        self.age = age

    # 实例方法   定义在类中的函数成为方法，自带一个self参数
    def show(self):
        print(f'姓名{self.name}，年龄{self.age}')


stu1 = Student('xx', 21)
stu2 = Student('yy', 20)

# 为stu2动态绑定一个属性
stu2.gender = '男'
print(stu2.name, stu2.age, stu2.gender)


# 为stu1动态绑定一个方法
def introduce():
    print('-----------stu1的方法-------------')


stu1.fun = introduce  # 函数不加括号，加括号表示调用，这里是赋值
stu1.fun()
