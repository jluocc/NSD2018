

# 此示例示意字典关键字传参
def myfun1(a, b, c):
    print("a的值是:", a)
    print("b的值是:", b)
    print("c的值是:", c)


d1 = {'c': 33, 'b':22, 'a':11}
# myfun1(d1['a'], d1['b'], d1['c'])
# myfun1(a=d1['a'], b=d1['b'], c=d1['c'])
myfun1(**d1) # 等同于myfun1(a=11,b=22,c=33)
d2 = {'c': 33, 'b':22, 'a':11, 'd':44}
# myfun1(**d2)  # 报错







