# 练习:
#   1. 写一个lambda表达式:
#       fx = lambda n: ...
#     此表达式创建的函数判断n这个数的2次方+1能否被5整除,如果能整除返回True,否则返回False
#     如:
#       print(fx(3))  # True
#       print(fx(4))  # False
  
# fx = lambda n: (n ** 2 + 1) % 5 == 0
fx = lambda n: True if (n ** 2 + 1) % 5 == 0 else False

print(fx(3))  # True
print(fx(4))  # False
    