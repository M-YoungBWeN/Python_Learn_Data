class Person:
    def eat(self):
        print('人吃饭')


class Cat:
    def eat(self):
        print('猫吃鱼')


class Dog:
    def eat(self):
        print('狗吃骨')


# 定义一个函数
def fun(obj):  # 传入的是一个对象obj
    obj.eat()  # 调用传入对象的eat()方法


# 创建三个对象
per = Person()
cat = Cat()
dog = Dog()

# 调用fun()函数
fun(per)  # Python中的多态，不关心对象的数据类型，只关心对象是否具有同名方
fun(cat)
fun(dog)
