#   1. 编写函数 fun,其功能是计算下列多项式的和
#     f(n) = 1 + 1/1! + 1/2! + 1/3! + 
#        ...... + 1/n!
#   求当n等20时,此函数的值

from math import factorial as fac

# 方法1
# def f(n):
#     s = 0
#     for x in range(n + 1):
#         s += 1 / fac(x)
#     return s

# 方法2
def f(n):
    s = sum(map(lambda x: 1 / fac(x),
                range(n + 1)))
    return s

print("f(20)=", f(20))



