lst = ['hello', 'world', 'python', 'and', 'pyqt']
print('原列表：', lst, id(lst))
lst.append('new!')
print('在尾部添加后:', lst, id(lst))

lst.insert(3, '666')
print('在任意位置添加后：', lst, id(lst))

lst.remove('hello')
print('删除后：', lst, id(lst))

# pop() 将元素取出再删除
print(lst.pop(2))
print('取出删除后：', lst, id(lst))

# clear()清空列表的所有元素
lst.clear()
print('清空元素后的列表：', lst, id(lst))
print('-'*20)

lst2 = ['hello', 'world', 'python', 'and', 'pyqt']
# reverse()列表的逆向
lst2.reverse()
print('逆向后的列表：', lst2, id(lst2))

# copy()拷贝列表
new_lst2 = lst2.copy()
print('原列表：', lst2, id(lst2))
print('拷贝的列表：', new_lst2, id(new_lst2))

# 列表内容的修改
new_lst2[2] = 'SQL'
print('修改后的列表：',new_lst2, id(new_lst2))

