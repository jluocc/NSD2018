class A:
    def m(self):
        print("A.m")
class B(A):
    pass
    # def m(self):
    #     print("B.m")
class C(B):
    def m(self):
        print("C.m")
c = C()
c.m()  # C.m
super(C, c).m()  # B.m
super(B, c).m()  # A.m
    