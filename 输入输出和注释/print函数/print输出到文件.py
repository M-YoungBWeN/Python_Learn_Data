fp = open('note.txt', 'w')  # 打开文件 w-->write
print('我是输出的文件', file=fp)   # 写入文件
fp.close()  # 关闭文件
