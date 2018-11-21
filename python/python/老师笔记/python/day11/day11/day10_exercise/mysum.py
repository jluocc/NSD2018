#   2. 给出一个整数n,写一个函数来计算
#     1 + 2 + 3 + 4 + ... + n 的值并返回结果
#     要求用函数来做
#     如:
#       def mysum(n):
#           ...
#       print(mysum(100))  # 5050
#       print(mysum(10))  # 55

# 方法1
# def mysum(n):
#     s = 0
#     for x in range(1, n + 1):
#         s += x
#     return s

def mysum(n):
    return sum(range(1, n + 1))

print(mysum(100))  # 5050
print(mysum(10))  # 55
