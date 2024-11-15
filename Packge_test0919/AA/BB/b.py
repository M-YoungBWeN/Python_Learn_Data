import os


def funb():
    # file_path = './data.txt'
    file_path = os.path.join(os.path.dirname(__file__), 'data.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)

    file_path2 = os.path.join(os.path.dirname(__file__), 'DataSet', 'data2.txt')
    with open(file_path2, 'r', encoding='utf-8') as file:
        data2 = file.read()
    print(data2)
















"""
相对路径相对的是当前工作目录，而不是相对于b.py的路径

file_path = os.path.join(os.path.dirname(__file__),'data.txt')
    第一部分 os.path.dirname(__file__)
        返回了指向当前文件(b.py)的绝对路径
    第二部分 os.path.join((b.py)的绝对路径,'data.txt')
        将(b.py)的绝对路径和data.txt组合为一个路径
        
        
    print("第一部分：",os.path.dirname(__file__))
    print("第二部分：",file_path)
"""