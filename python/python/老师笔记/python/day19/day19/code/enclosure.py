# enclosure.py

class A:
    def __init__(self):
        self.__p1 = 100  # 私有属性
        print("self.__p1=", self.__p1)

    def __m(self):
        '''这是私有方法,此方法只能用此类的方法来调用,不能在其它地方调用'''
        print("A.__m方法被调用")

    def dowork(self):
        '此方法可以调用私有实例变量和实例方法'
        self.__m()
        print("dowork内.self.__p1=", self.__p1)

class B(A):
    '''此类示意子类不能调用父类的私有成员'''
    def test(self):
        self.__m()  # 出错
        print(self.__p1)  # 出错

a = A()
# print(a.__p1)  # 错误,不允许访问私有属性
# a.__m()  # 无法调用
a.dowork()
# a.test()  # 出错




