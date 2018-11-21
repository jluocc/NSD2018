# 练习:
# 求: 1**2 + 2**2 + 3**2 + ... + 9**2的和

# 求: 1**3 + 2**3 + 3**3 + ... + 9**3的和

# 求: 1**9 + 2**8 + 3**7 + ... + 9**1的和


# 求: 1**2 + 2**2 + 3**2 + ... + 9**2的和
def power2(x):
    return x ** 2
# 方法1
# s = 0
# for x in map(power2, range(1, 10)):
#     s += x
# print(s)
# 方法2
# m = map(power2, range(1, 10))
# print(sum(m))
# 方法3
print(sum(map(power2, range(1, 10))))

# 求: 1**3 + 2**3 + 3**3 + ... + 9**3的和
print(sum(map(lambda x:x**3, range(1, 10))))

# 求: 1**9 + 2**8 + 3**7 + ... + 9**1的和
print(sum(map(pow,
              range(1, 10),
              range(9, 0, -1))))

