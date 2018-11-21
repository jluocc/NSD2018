# globals_locals.py

a = 1
b = 2
c = 3

def fn(c, d):
    e = 300
    # 此时有几个局部变量
    print("locals() 返回:", locals())
    print("globals() 返回:", globals())
    print(c)  # 访问局部变量100
    print(globals()['c'])  # 访问全局变量c


fn(100, 200)
