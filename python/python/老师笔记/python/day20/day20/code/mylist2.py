
# 此示例示意复合赋值算术运算符的重载方法
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        print("__add__方法被调用")
        return MyList(self.data + rhs.data)

    def __iadd__(self, rhs):
        print("__iadd__被调用")
        self.data.extend(rhs.data)
        return self

L1 = MyList(range(1, 4))
L2 = MyList([4, 5, 6])
print(id(L1))
L1 += L2  # L1 = L1 + L2
print(id(L1))
print("L1=", L1)
print("L2=", L2)

