#   2. 写一个lambda表达式来创建函数,此函数返回两个形参变量的最大值
#     def mymax(x, y):
#         ...
    
#     mymax = lambda ...
#     print(mymax(100, 200))  # 200
#     print(mymax("ABC", "123"))  # ABC

# def mymax(x, y):
#     return max(x, y)

# def mymax(x, y):
#     return x if x > y else y

# mymax = lambda x, y: max(x, y)
mymax = lambda x, y: x if x > y else y

print(mymax(100, 200))  # 200
print(mymax("ABC", "123"))  # ABC
