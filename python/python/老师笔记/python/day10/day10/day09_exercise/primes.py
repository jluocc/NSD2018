#   素数/质数
#     2, 3, 5, 7, 11, 13
#   1. 写一个函数isprime(x) 判断x是否是素数.如果是素数返回True,否则返回False
#     def isprime(x):
#         ...
#     print(isprime(4)) # False
#     print(isprime(5)) # True

#   2. 写一个函数prime_m2n(m, n)  返回从m开始,到n结束的范围内的素数(不包含n),返回这些素数的列表,并打印
#     如:
#       L = prime_m2n(5, 10)
#       print(L)  # [5, 7]
#   3. 写一个函数primes(n)  返回指定范围n以内的素数(不包含n)的全部素数的列表,并打印这些素数
#       L = primes(10)
#       print(L)  # [2, 3, 5, 7]
#      1) 打印100以内的全部素数
#      2) 打印200以内的全部素数的和



#   1. 写一个函数isprime(x) 判断x是否是素数.如果是素数返回True,否则返回False
def isprime(x):
    # 如果x小于2不是素数
    if x < 2:
        return False
    # 如果x大于等于2,则用x对2...x-1的数求余.
    for i in range(2, x):
        # 如果余数为0则不是素数
        if x % i == 0:
            return False
    # 否则就为素数
    return True

print(isprime(4)) # False
print(isprime(5)) # True

#   2. 写一个函数prime_m2n(m, n)  返回从m开始,到n结束的范围内的素数(不包含n),返回这些素数的列表,并打印
def prime_m2n(m, n):
    L = []
    for x in range(m, n):
        # 判断如果x是素数,则加到列表L中
        if isprime(x):
            L.append(x)
    return L

L = prime_m2n(5, 10)
print(L)  # [5, 7]

#   3. 写一个函数primes(n)  返回指定范围n以内的素数(不包含n)的全部素数的列表,并打印这些素数
def primes(n):
    return prime_m2n(0, n)

L = primes(10)
print(L)  # [2, 3, 5, 7]
# 1) 打印100以内的全部素数
print(primes(100))
# 2) 打印200以内的全部素数的和
print(sum(primes(200)))

