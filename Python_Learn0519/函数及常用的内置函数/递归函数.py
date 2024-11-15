"""
递归：在函数体内部调用函数
调用、终止
"""


#
# 阶乘的计算
def fac(n):  # n的阶乘，n!=n*(n-1)! 直到1!=1
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(3))


#
# 斐波那契数列
def f(n):  # 第n项的斐波那契数 f(n)=f(n-1)+f(n-2)
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


print(f(5))
for i in range(1,11):
    print(f(i),end=' ')

print()
print('-'*20)
