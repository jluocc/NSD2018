
# 此示例示意复合赋值算术运算符的重载方法
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __neg__(self):
        '''重载负号运算符'''
        # L = [-x for x in self.data]
        # L = (-x for x in self.data)
        L = map(lambda x:-x, self.data)
        return MyList(L)

L1 = MyList([1, -2, 3, -4, 5])
L2 = -L1
print(L2)  # MyList([-1, 2, -3, 4, -5])
# L3 = +L1
# print(L3)  # MyList([1, 2, 3, 4, 5])

