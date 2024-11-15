"""
重写show()方法
重写父类的方法，方法名称需要与父类方法名相同
"""


class Person:  # 父类，默认继承了object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shou(self):
        print(f'姓名{self.name},年龄{self.age}')


class Student(Person):  # 子类A
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)  # 调用父类的初始化方法  super()在子类中调用父类的方法，多用于类的继承关系
        #   # super()函数更加灵活和动态，能够准确调用多级继承中的父类方法，而父类名称较为静态，在直接继承中使用更为方便
        #   # Person.__init__(self,name,age)
        self.stu_no = stu_no

    def shou(self):  # 重写show()方法
        super().shou()
        print('学号：', self.stu_no)


class Doctor(Person):  # 子类B
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def shou(self):  # 重写show()方法
        print(f'姓名{self.name},年龄{self.age},部门{self.department}')


stu = Student('xx', 20, 1001)
doc = Doctor('yy', 35, '外科')
stu.shou()
doc.shou()
