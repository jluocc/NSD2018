# 练习:
#   写一个函数,mysum 可以传入任意个数字的实参,此函数调用将返回实参的和
#   如:
#     def mysum(*args):
#         ...
    
#     print(mysum())  # 0
#     print(mysum(1, 2, 3))  # 6


def mysum(*args):
    # s = 0
    # for x in args:
    #     s += x
    # return s
    return sum(args)

print(mysum())  # 0
print(mysum(1, 2, 3))  # 6
