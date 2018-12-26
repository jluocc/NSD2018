# 练习:
#   1. 写一个生成器函数,给出开始值begin,和终止值end,此生成器函数生成begin~end 范围内的全部素数(不包含end)
#     如:
#       def prime(begin, end):
#           ...

#       L = list(prime(10, 20))
#       print(L)  # [11, 13, 17, 19]


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def primes(begin, end):
    for x in range(begin, end):
        # 如果x是素数,则用yield把这个送回给调用者
        if is_prime(x):
            yield x


L = list(primes(10, 20))
print(L)  # [11, 13, 17, 19]
# 求: 200以内全部素数的和:
print(sum(primes(0, 200)))
