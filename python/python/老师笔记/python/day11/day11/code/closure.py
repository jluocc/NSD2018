# closure.py

# 定义很多个函数每个函数求 x**y次方,y是可变的
# 示意
def pow2(x):
    return x**2

def pow3(x):
    return x**3

# ...
def pow99(x):
    return x**99

# 以下用闭包来实现
def make_power(y):
    def fn(x):
        return x ** y
    return fn

pow2 = make_power(2)  # pow2绑定一个闭包
print("5的平方是:", pow2(5))  # 25

pow3 = make_power(3)
print("5的立方是:", pow3(5))
pow99 = make_power(99)
print('2的99次方是:', pow99(2))

