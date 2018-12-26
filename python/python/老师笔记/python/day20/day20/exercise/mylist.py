# 练习:
#   实现两个自定义的列表相加操作
#     class MyList:
#         ...  # 此处代码自己实现
    
#     L1 = MyList(range(1, 4))
#     L2 = MyList([4, 5, 6])
#     L3 = L1 + L2
#     print(L3)  # MyList([1, 2, 3, 4, 5, 6])
#     L4 = L2 + L1
#     print(L4)  # MyList([4, 5, 6, 1, 2, 3])
#     L5 = L1 * 3
#     print(L5)  # MyList([1,2,3,1,2,3,1,2,3])


class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        return MyList(self.data * rhs)

L1 = MyList(range(1, 4))
L2 = MyList([4, 5, 6])
L3 = L1 + L2
print(L3)  # MyList([1, 2, 3, 4, 5, 6])
L4 = L2 + L1
print(L4)  # MyList([4, 5, 6, 1, 2, 3])
L5 = L1 * 3
print(L5)  # MyList([1,2,3,1,2,3,1,2,3])
