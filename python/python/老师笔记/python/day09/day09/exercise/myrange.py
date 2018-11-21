# 练习:
#   写一个myrange函数,参数可以传入1~3个,实际含义与range函数相同
#   此函数返回符合range(...) 函数的列表
#   如:
#     L = myrange(4)
#     print(L)  # [0, 1, 2, 3]
#     L = myrange(4, 6)
#     print(L)  # [4, 5]
#     L = myrange(1, 10, 3)
#     print(L)  # [1, 4, 7]
#   (注: 可以调用range)


def myrange(a, b=None, c=None):
    if b is None:
        start = 0
        stop = a  # 第一个数
    else:
        start = a
        stop = b
    if c is None:
        step = 1
    else:
        step = c
    # print("开始值:", start,
    #       "结束值:", stop,
    #       '步长', step)
    return list(range(start, stop, step))

L = myrange(4)
print(L)  # [0, 1, 2, 3]
L = myrange(4, 6)
print(L)  # [4, 5]
L = myrange(1, 10, 3)
print(L)  # [1, 4, 7]

