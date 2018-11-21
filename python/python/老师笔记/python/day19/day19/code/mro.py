# mro.py


# 此示例示意__mro__类属性和用法
class A:
    def go(self):
        print("A")

class B(A):
    def go(self):
        print("B")
        super(B, self).go()  # C

class C(A):
    def go(self):
        print("C")
        super().go()   # A

class D(B, C):
    def go(self):
        print("D")
        super().go()  # B

d = D()
d.go()
    