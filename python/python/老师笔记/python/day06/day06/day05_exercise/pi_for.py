# 3.
# 编写程序求下列多项式的值:
#     Sn = 1/1 - 1/3 + 1/5 - 1/7 + .....
#     1) 求1000000个这样的分数相加的和是多少?
#     2) 将上一步的和乘以4打印出来,是多少?

Sn = 0.0
fenmu = 1  # 代表分母
sign = 1  # 代表正负符号
# while i < 100000000:
for _ in range(1000000):
    r = sign / fenmu
    Sn += r  # 累加

    sign *= -1
    fenmu += 2

print("Sn=", Sn)
print("Sn*4=", Sn * 4)

