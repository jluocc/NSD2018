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
    

# print(A.v)  # 0 直接访问类变量
value = A.get_v()  # 相调用A类的方法来取值
print("value =", value)  # 0

A.set_v(999)
print(A.get_v())  # 999





