# 此示例示意return语句的作用和用法


def say_hello2():
    print("hello aaa")
    print("hello bbb")
    print("hello ccc")
    # 此处相当于有条语句 return None

r = say_hello2()  # 调用
print("r=", r)  # None

