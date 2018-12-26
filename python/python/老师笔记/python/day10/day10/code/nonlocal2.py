

# 3. 当有两层或两层以上函数嵌套时,访问nonlocal变量只对最近的一层的变量进行操作
v = 100
def f1():
    v = 200
    def f2():
        v = 300
        def f3():
            nonlocal v
            v = 400  # 此时改变f2里的v
        f3()
        print("f2.v=", v)  # 400
    f2()
f1()






