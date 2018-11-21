# del_method.py

# 此示例示意析构方法的定义和自动调用 
class Car:
    def __init__(self, info):
        self.info = info
        print("汽车:", info, "对象被创建")

    def __del__(self):
        '''这是析构方法,形参只有一个self'''
        print("汽车", self.info, "被销毁")

c1 = Car("BYD E6")
c2 = c1  # c2绑定谁?
del c1  # 删除变量c1
input("按回车键继续执行程序: ")
print("程序正常退出")



