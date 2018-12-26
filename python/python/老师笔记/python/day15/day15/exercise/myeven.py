# 练习:
#   写一个生成器函数 myeven(start, stop) 用来生成从start开始到stop结束区间内的一系列偶数(不包含stop)
#   如:
#     def myeven(start, stop):
#         ...  # 此处自己实现

#     evens = list(myeven(10, 20))
#     print(evens) # [10, 12, 14, 16, 18]
#     for x in myeven(5, 10):
#         print(x)  # 6  8
#     L = [x for x in myeven(0, 10)]
#     print(L) # [0, 2, 4, 6, 8]



def myeven(start, stop):
    for x in range(start, stop):
        if x % 2 == 0:
            yield x


evens = list(myeven(10, 20))
print(evens) # [10, 12, 14, 16, 18]
for x in myeven(5, 10):
    print(x)  # 6  8
L = [x for x in myeven(0, 10)]
print(L) # [0, 2, 4, 6, 8]
