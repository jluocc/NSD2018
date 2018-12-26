# 此示例示意写一个函数,此函数的功能是给它两个数据,让它把最大值的数据打印出来


def mymax(a, b):
    m = a
    if b > m:
        m = b
    print("最大值的数据是:", m)


mymax(100, 200)
mymax("ABC", "123")



