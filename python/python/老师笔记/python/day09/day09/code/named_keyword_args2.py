# named_keyword_args.py


# 此示例示意命名关键字形参的定义的方式和调用方法
def f2(a, b, *args, c, d):
    print(a, b)
    print(args)
    print(c, d)


# f2(1, 2, 3, 4, d=200, c=100)
f2(11,22, 33, **{'c':11, 'd':22})

