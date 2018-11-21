# 练习:
#   1. 写一个函数 myadd2, 实现给出两个数,返回这两个数的和
#     如:
#       def myadd(x, y):
#           .....
#       a = int(input("请输入第一个数: "))
#       b = int(input("请输入第二个数: "))
#       print("您输入的这两个数的和是", myadd2(a, b))



def myadd2(x, y):
    z = x + y
    return z
    # return x + y


a = int(input("请输入第一个数: "))
b = int(input("请输入第二个数: "))
print("您输入的这两个数的和是", myadd2(a,b))
