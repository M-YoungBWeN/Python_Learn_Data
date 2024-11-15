#
#
# sort()
lst = [51, 5, 971, 51, 54, 9, 97, 4, 59, 1, 130, 14, 49]
lst2 = lst.copy()

# sort()默认升序
lst.sort()
print(lst)

# sort()降序
lst2.sort(reverse=True)
print(lst2)

# sort()大写字母比小写字母ASCII小，所以默认先排大写再排小写
lss = ['China', 'Abb', 'abdd', 'couidd', 'GOdd']
lss.sort()
print(lss)
lss.sort(reverse=True)
print(lss)

# sort()不区分大小写排序
lss.sort(key = str.lower)
print(lss)


print('-'*20)
#
#
# sorted() 相比sort()，sorted()会拷贝一份再排序
lst = [51, 5, 971, 51, 54, 9, 97, 4, 59, 1, 130, 14, 49]
lss = ['China', 'Abb', 'abdd', 'couidd', 'GOdd']
new_lst = sorted(lst)
print(new_lst)
# 忽略大小写排序
new_lss = sorted(lss, key=str.lower)
print(new_lss)
