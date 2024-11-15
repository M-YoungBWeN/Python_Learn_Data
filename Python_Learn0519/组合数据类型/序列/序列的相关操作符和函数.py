s = '麻花与千层饼lll'
print('杨 存在吗', ('杨' in s))
print('麻花 存在吗', ('麻花' in s))
print('m 不存在吗', ('m' not in s))

#
# 内置函数使用
print('len()', len(s))
print('max()', max(s))  # 按照ASCII计算
print('min()', min(s))
print('-' * 20)
#
# 序列对象的方法。方法：打点调用
print('与 第一次出现的位置：', s.index('与'))
print('统计l的个数：', s.count('l'))
