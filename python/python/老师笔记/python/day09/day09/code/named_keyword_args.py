# named_keyword_args.py


# 此示例示意命名关键字形参的定义的方式和调用方法
def f1(*, c, d): #*之后的形参为命名关键字形参
    print("c=", c)
    print("d=", d)

# f1(3, 4)  # 报错
f1(d=4, c=3)  # 关键字正确
d1 = {'c':30, 'd': 40}
f1(**d1)
