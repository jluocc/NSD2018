# 4. 给出一个整数n,写一个函数来计算
#     1+2**2+3**3+...+ n**n的和
# (n给一个小点的数)

# 方法 1
# def f(n):
#     s = 0
#     for x in range(1, n + 1):
#         s += x ** x
#     return s

# 方法2
def f(n):
    return sum(map(
        lambda x:x**x,
        range(1, n+1)
        ))

print("f(2) = ", f(2))
print("f(5) = ", f(5))
    


