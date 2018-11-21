#   1. 编写程序求 1 ~ 20的阶乘的和
#     即:
#       1! + 2! + 3! + ... + 20!

# 方法1
# s = 0
# for x in range(1, 21):
#     # 计算x的阶乘
#     r = 1
#     for y in range(1, x + 1):
#         r *= y
#     # 把x! r加到s中
#     s += r

# 方法2
# def myfac(x):
#     r = 1
#     for y in range(1, x + 1):
#         r *= y
#     return r

# s = 0
# for x in range(1, 21):
#     # 计算x的阶乘
#     r = myfac(x)
#     # 把x! r加到s中
#     s += r

# 方法3
# def myfac(x):
#     r = 1
#     for y in range(1, x + 1):
#         r *= y
#     return r

# s = sum(map(myfac, range(1, 21)))

# 方法4
import math
s = sum(map(math.factorial, range(1, 21)))

print(s)  # 

