
# 此示例示意in /not in 运算符重载方法
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __contains__(self, e):
        '重载in 运算符,只需要判断 e是否在self里'

        return e in self.data

L1 = MyList([1, -2, 3, -4, 5])
print(3 in L1)  # True
print(3 not in L1)  # False
print(4 not in L1)  # True
print(4 in L1)  # False

