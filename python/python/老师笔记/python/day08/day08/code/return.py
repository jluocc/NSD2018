# 此示例示意return语句的作用和用法


def say_hello2():
    print("hello aaa")
    print("hello bbb")
    # return  # 等同于return None
    # return 1 + 2
    return [1, 2, 3, 3 + 1]
    print("hello ccc")

r = say_hello2()  # 调用
print("r=", r)  # None

print("程序结束")