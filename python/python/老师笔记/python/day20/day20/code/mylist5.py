
# 此示例示意 索引和切片 [] 运算符重载方法
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __getitem__(self, i):
        print("__getitem__被调用, i=", i)
        return self.data[i]

    def __setitem__(self, i, v):
        print("__setitem__: i=", i, "v=", v)
        # print("嘿嘿!")
        self.data[i] = v

    def __delitem__(self, i):
        print("__delitem__被调用 i=", i)
        del self.data[i]

L1 = MyList([1, -2, 3, -4, 5])
x = L1[2]  # x = L1.__getitem__(2)
print(x)
L1[1] = 2.2  # L1.__setitem(1, 2.2)
print(L1)

del L1[3]  # L1.__delitem(3)
print(L1)



