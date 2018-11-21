#   2. 写一个生成器函数 myxrange(start, stop, step) 来生成一系列整数
#      要求功能与range完全相同
#      不允许调用range函数和列表
#     然后用自己写的myxrange函数求 1 ~ 100内奇数的平方和

def myxrange(start, stop=None, step=1):
    # 调用开始和结束的值
    if stop is None:
        stop = start
        start = 0

    # 正向生成:
    if step > 0:
        while start < stop:
            yield start  # 生成当前值
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step  # 加上一个负数


L = [x**2 for x in myxrange(1, 101, 2)]
print(sum(L))
