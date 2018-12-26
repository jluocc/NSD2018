
# 此示例示意全局变量和局部变量
a = 100  # 全局变量
b = 200  # 全局变量

def fx(c):  # c是局部变量
    d = 400  # 局部变量
    a = 10000
    print(a, b, c, d)  # 优先访问局部变量

fx(300)
print('a =', a)  # 100
print('b =', b)
# print('c =', c)  # 出错
# print('d =', d)  # 出错


