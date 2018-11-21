
# 练习:
#   1. 写一个程序，输入一个数，用if语句计算这个数的绝对值,并打印出来
#   　　（要求: 不允许用abs(x) 函数)

x = int(input("请输入一个整数: "))
# if x >= 0:
#     print(x)
# else:
#     print(-x)
if x < 0:
    x = -x

print(x)