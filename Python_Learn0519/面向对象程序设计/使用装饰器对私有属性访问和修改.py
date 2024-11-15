class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    # 使用修饰器访问私有属性gender
    # 为什么要使用修饰器@property？ 使用修饰器@property后可以把方法当属性
    @property
    def gender(self):
        return self.__gender

    def gender_show(self):
        return self.__gender

    # 使用修饰器更改私有属性的值
    # 将gender属性设置为可写属性
    @gender.setter
    def gender(self, value):
        if value != '男' and value != '女':
            print('输入错误，默认为男')
            self.__gender = '男'
        else:
            self.__gender = value

    def ggender_change(self, value):
        if value != '男' and value != '女':
            print('输入错误，默认为男')
            self.__gender = '男'
        else:
            self.__gender = value


stu = Student('xx', '男')
print(stu.name, stu.gender)  # 这里的方法gender直接当属性来用，所以不加()
print(stu.name, stu.gender_show())  # 这里的方法没有被修饰器修饰，是个普通的方法，所以要加()才能调用

print('-' * 20)

stu.gender = '武装直升机'  # 直接把修饰器修饰的方法当成属性用
print(stu.name, stu.gender)

print('-' * 20)

stu.ggender_change('女')  # 普通方法需要加()才能调用
print(stu.name, stu.gender_show())
