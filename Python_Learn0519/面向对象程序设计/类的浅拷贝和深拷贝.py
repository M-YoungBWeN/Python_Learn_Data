"""
对象的赋值:把对象的地址传递了 没有开辟新的空间（不拷贝对象）
对象的浅拷贝copy:开辟了一个新的对象空间 没有为子对象开辟新的空间（不拷贝子对象）
对象的深拷贝deepcopy：源对象和子对象都做了拷贝
"""


class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 创建对象
cpu = CPU()
disk = Disk()
com = Computer(cpu, disk)

# 对象的赋值
com1 = com
print(com, com.cpu, com.disk)
print(com1, com1.cpu, com1.disk)

print('-' * 20)
# 对象的浅拷贝
import copy

com2 = copy.copy(com)
print(com, com.cpu, com.disk)
print(com2, com2.cpu, com2.disk)

print('-'*20)
# 对象的深拷贝
com3 = copy.deepcopy(com)
print(com, com.cpu, com.disk)
print(com3, com3.cpu, com3.disk)
