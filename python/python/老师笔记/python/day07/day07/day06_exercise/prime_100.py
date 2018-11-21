# 2. 计算出100以内的全部素数，将这些素数存于列表中，然后打印出列表中的这些素数

# 遍历1~100之间的数,如果这个数是素数,加入到一个列表中
L = []  # 此容器准备加入素数
for x in range(1, 101):
    # 如果x是素数,则把x加入到L中,否则跳过
    isprime = True  # 先假设x是素数
    # 如果x不是素数,就把isprime置为False
    if x < 2:
        isprime = False
    else:
        for i in range(2, x):
            if x % i == 0:  # 整除不是素数
                isprime = False
                break
    if isprime:  # 一定为素数
        L.append(x)

print("L = ", L)