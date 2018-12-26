# global.py


# 此示示意global语句的用法
v = 100
def f1():
    global v  # 全局声明
    v = 200

f1()
print('v=', v)  # ???


