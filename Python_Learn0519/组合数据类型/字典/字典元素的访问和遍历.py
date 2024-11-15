d = {'hello': 10, 'world': 20, 'python': 30}

#
# 访问字典中的元素
print(d['hello'])  # 用d[key]访问
print(d.get('hello'))  # 用d.get(key)访问

# 两种访问方式有差别。用方法访问时空值会返回None或返回自己设置的值，而d[]会报错
print(d.get('java'))
print(d.get('java', '不存在'))

print('-' * 20)
#
# 元组的遍历
for item in d.items():
    print(item)

for key, value in d.items():    # 遍历时分别获取key value
    print(key, value)
