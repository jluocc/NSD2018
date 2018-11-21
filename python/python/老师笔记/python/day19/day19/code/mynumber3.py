# mynumber2.py


class MyNumber(object):
    '''此类用于定义一个自定义的数字类型'''
    def __init__(self, value):
        self.data = value  # data数据

    # def __str__(self):
    #     '''重写object类中的__str__(obj)'''
    #     print("MyNumber.__str__被调用")
    #     return "数字%d" % self.data

    def __repr__(self):
        return "MyNumber(%d)" % self.data

n1 = MyNumber(100)
s1 = str(n1)  # ?????
print(s1)

