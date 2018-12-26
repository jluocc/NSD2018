# myinteger.py

# 此示例示意用生成器函数创建生成从0开始到n结束的一系列整数(不包含n)
def myinteger(n):  # integer(整数)
    i = 0  # 设置初始值为0
    while i < n:
        yield i  # 生成i给next(it) 调用
        i += 1  # 为生成下一个数做准备

for x in myinteger(10000000000000000000):
    print(x)
