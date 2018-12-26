
# 4. global变量列表里的变量名不能出现在函数的形参列表里

v = 100
def f1(v):
    # global v  # 报错 SyntaxError: name 'v' is parameter and global
    print(v)  # 100

f1(200)


