# 练习:
#   写一个函数hello,部分代码如下:
#     count = 0
#     def hello(name):
#         print("你好", name)
#         ... 此处略
#   当调用hello函数时,全局变量count自动做加1操作来记录hello被调用的次数
#   如:
#     hello("Tom")
#     hello("Jerry")
#     print("hello函数共被调用%d次" % count)  # 2


count = 0
def hello(name):
    print("你好", name)
    
    global count  # 全局声明
    count += 1

hello("Tom")
hello("Jerry")
print("hello函数共被调用%d次" % count)  # 2
hello("Jerry")
hello("Jerry")
hello("Jerry")
hello("Jerry")
hello("Jerry")
hello("Jerry")
print("hello函数共被调用%d次" % count)  # 8

