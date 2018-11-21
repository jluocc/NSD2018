#   2. 写一个函数mymax3,返回三个数中最大的一个值
#     def mymax3(a, b, c):
#         .... # 此处自己实现
    
#     print(mymax3(100, 300, 200))  # 300
#     print(mymax3("ABC", "123", "abc")) # abc

# 方法1
# def mymax3(a, b, c):
#     zuida = a
#     if b > zuida:
#         zuida = b
#     if c > zuida:
#         zuida = c
#     return zuida

# 方法2
# def mymax3(a, b, c):
#     z = a if a > b else b
#     z = z if z > c else c
#     return z

def mymax3(a, b, c):
    return max(a, b, c)
    # z = max(a, b)
    # z = max(z, c)
    # return z


print(mymax3(100, 300, 200))  # 300
print(mymax3("ABC", "123", "abc")) # abc
