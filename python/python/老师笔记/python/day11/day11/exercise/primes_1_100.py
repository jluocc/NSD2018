# 练习:
#   1. 把1～１００之间的全部素数放在列表primes中
#   def isprime(x):
#       ...
#   ...


def isprime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
    

primes = [x for x in filter(
    isprime,
    range(100)
)]

print(primes)
