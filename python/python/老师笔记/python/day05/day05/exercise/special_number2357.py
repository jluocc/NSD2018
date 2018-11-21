# 2. 求 1~100之间所有不能被2,3,5,7整除的数
#     1) 打印这些数
#     2) 打印这些数的和

he = 0

# for x in range(1, 100):
#     if x % 2 == 0:
#         continue
#     if x % 3 == 0:
#         continue
#     if x % 5 == 0:
#         continue
#     if x % 7 == 0:
#         continue
#     print(x)
#     he += x

for x in range(1, 100):
    if (x % 2 == 0
    or x % 3 == 0
    or x % 5 == 0
    or x % 7 == 0):
        continue
    print(x)
    he += x


print("以上数字的和是:", he)


