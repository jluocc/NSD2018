# 练习:
#   写一个函数min_max(...) 函数,
#    此函数至少要传一个参数,并返回全部这些数数的最小值,最大值(形成元组,最小在前,最大值在后)
#    调用此函数,得到最小值和最大值并打印出来
#   如:
#     def min_max(...):
#         ...

#     print(min_max(10, 20, 30))  # (10,30)
#     x, y = min_max(8, 6, 4, 3, 9, 2, 1)
#     print("最小值是:", x)
#     print("最大值是:", y)
#     print(min_max())  # 没有实参报错



# 方法1
# def min_max(a, *args):
#     zuixiao = a
#     for x in args:
#         if x < zuixiao:
#             zuixiao = x

#     # 求最大
#     zuida = a
#     for x in args:
#         if x > zuida:
#             zuida = x
#     return (zuixiao, zuida)

# 方法2    
# def min_max(a, *args):
#     zuixiao = min(args) # 先从第二个起的参数选出最小值
#     if a < zuixiao:
#         zuixiao = a
    
#     zuida = max(args)
#     if a > zuida:
#         zuida = a

#     return (zuixiao, zuida)

# 方法3
def min_max(a, *args):
    zuixiao = min(a, *args)
    zuida = max(a, *args)
 
    return (zuixiao, zuida)


print(min_max(10, 20, 30))  # (10,30)
x, y = min_max(8, 6, 4, 3, 9, 2, 1)
print("最小值是:", x)  # 1
print("最大值是:", y)  # 9
# print(min_max())  # 没有实参报错
