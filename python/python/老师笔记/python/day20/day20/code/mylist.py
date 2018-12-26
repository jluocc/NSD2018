
# 此示例示意反向算术运算符的重载方法
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        print("__mul__被调用")
        return MyList(self.data * rhs)

    def __rmul__(self, lhs):
        print("__rmul__被调用")
        return MyList(self.data * lhs)

L1 = MyList(range(1, 4))
L2 = MyList([4, 5, 6])
L5 = L1 * 3  # L1.__mul__(3)
print(L5)  # MyList([1,2,3,1,2,3,1,2,3])

L6 = 3 * L1  # L1.__rmul__(3)
print(L6)