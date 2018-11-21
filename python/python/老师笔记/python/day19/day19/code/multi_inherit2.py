# multi_inherit2.py


# 此示例示意多继承标识符冲突的问题

# 小李写了一个类A
class A:
    def m(self):
        print("A.m()被调用")

# 小张写了一个类B
class B:
    def m(self):
        print("B.m()被调用")

# 小王感觉小张和小李写的两个类自己都能用
class AB(A, B):
    pass
    # def m(self):
    #     print("AB.m()被调用")

ab = AB()
ab.m()  # 会???





