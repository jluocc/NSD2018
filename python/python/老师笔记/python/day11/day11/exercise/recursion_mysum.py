# 练习:
#   用递归的方式求1 + 2 + 3 + ...  + n 的和
#   def mysum(n):
#       ...
#   print(mysum(100))  # 5050


def mysum(n):
    if n == 1:
        return 1
    return n + mysum(n - 1)

print(mysum(100))  # 5050
# print(mysum(1000))  # 崩溃 crash

