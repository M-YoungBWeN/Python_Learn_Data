"""
Student类创建多个对象
"""


class Student:
    school = 'YTU'  # 类属性

    # 初始方法方法 没有实例属性可以不写初始化方法
    def __init__(self, name, age):  # name，age是方法的参数 是局部变量 作用于整个__init__方法
        self.name = name  # = 左侧是实例属性，右侧是局部变量。
        self.age = age

    # 实例方法   定义在类中的函数成为方法，自带一个self参数
    def show(self):
        print(f'姓名{self.name}，年龄{self.age}')


stu1 = Student('xx', 18)
stu2 = Student('lkl', 20)
stu3 = Student('ppp', 19)
stu4 = Student('zz', 18)
stu5 = Student('yy', 21)

lst = [stu1, stu2, stu3, stu4, stu5]  # 列表存储的是Student对象
for item in lst:  # item 是列表的元素，是Student对象
    item.show()  # 对象名打点调用实例方法
