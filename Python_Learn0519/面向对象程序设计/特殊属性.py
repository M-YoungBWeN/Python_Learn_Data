# 测试特殊属性
class A:
    pass


class B:
    pass


class C(B, A):

    def __init__(self, nn):
        self.nn = nn

    def cc(self):
        print("cc")


c = C(2)

print('对象的属性字典', c.__dict__)  # 对象的属性字典
print('对象所属的类  ', c.__class__)  # 对象所属的类
print('类的父类     ', C.__bases__)  # 类的父类
print('类的一个父类  ', C.__base__)  # 类的一个父类
print('类层次结构    ', C.__mro__)  # 类层次结构
print('子类列表     ', A.__subclasses__())  # 子类列表 带括号是因为subclasses是一个方法
