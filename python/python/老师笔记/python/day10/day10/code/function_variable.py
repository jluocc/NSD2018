# function_variable.py


# 此示例示意函数名绑定函数,函数名是变量 
def fn():
    print("hello world")

f1 = fn
print(f1)  # <function fn at 0x7f0bb2eb0f28>

fn()  # hello world
f1()  # hello world
f2 = fn()  #
print(f2)  # None
