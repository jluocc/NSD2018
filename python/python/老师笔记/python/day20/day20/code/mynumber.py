# mynumber.py

# 此示例示意 运算符重载
class MyNumber:
    '自定义数字'
    def __init__(self, value):
        self.data = value

    def __repr__(self):
        return "MyNumber(%d)" % self.data
    
    def __add__(self, other):
        '''加号运算符的重载方法'''
        print("__add__被调用")
        v = self.data + other.data
        obj = MyNumber(v)  # 创建一个新对象
        return obj
    
    def __sub__(self, rhs):
        return MyNumber(self.data - rhs.data)

n1 = MyNumber(100)
n2 = MyNumber(200)
# n3 = n1.__add__(n2)  # MyNumber(300)
n3 = n1 + n2  # 等同于n1.__add__(n2)
print(n1, "+", n2, "=", n3)
n4 = n1 - n2
print(n1, "-", n2, "=", n4)
