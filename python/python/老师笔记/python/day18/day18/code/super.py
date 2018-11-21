# super.py

# 此示例示意用super函数显式的调用被覆盖的方法
class A:
    def work(self):
        print("A.work被调用")

class B(A):
    def work(self):
        '''此方法会覆盖父类的work方法'''
        print("B.work被调用")

    def mywork(self):
        # 调用自己(B类)的方法
        self.work()
        # 调用父类(A类)的方法 
        super(B, self).work()
        super().work()

b = B()
# b.work()  # B.work被调用
# # A.work(b)  # A.work被调用
# super(B, b).work()  # A.work被调用

b.mywork()

