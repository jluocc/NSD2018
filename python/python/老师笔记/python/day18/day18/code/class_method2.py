# class_method.py


# 此示例示意类方法的定义及调用
class A:
    v = 0

    @classmethod
    def get_v(cls):
        return cls.v  # 获取类变量v的值

    @classmethod
    def set_v(cls, value):
        cls.v = value  # 设置类变量v=value

a = A()  # 创建的实例对象
print(a.get_v())  # 借助对象来调用类方法
a.set_v(100)  # 借助对象来设置类变量v
print(a.get_v())  # 100
print(A.v)  # 100





