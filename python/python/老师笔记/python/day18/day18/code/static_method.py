# static_method.py


#此示例示意静态方法的定义和使用
class A:
    @staticmethod
    def myadd(a, b):
        '''这是静态方法'''
        return a + b

# 用类来调用静态方法
print(A.myadd(100, 200))  # 300
a = A()
# 用此类的实例来调用静态方法
print(a.myadd(300, 400))  # 700

# print(myadd(1, 2))






