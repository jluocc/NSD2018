# closure2.py

# 用闭包来创建的任意的
#   f(x)  = a*x**2 + b*x + c 的函数

def get_fx(a, b, c):
    def fx(x):
        return a*x**2 + b*x + c
    return fx

f123 = get_fx(1, 2, 3)
print(f123(20))
print(f123(50))

f456 = get_fx(4, 5, 6)
print(f456(20))
print(f456(50))





