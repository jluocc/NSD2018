# 猜数字游戏:
#   随机生成一个0~100之间的整数,用变量x绑定
#   让用户输入一个数y.输出猜数字的结果
#       1) 如果y等于生成的数x,则提示"恭喜您猜对了",并退出程序
#       2) 如果y大于x,则提示"您猜大了", 然后继续猜下一次
#       3) 如果y小于y,则提示"您猜小了", ...
#     直到猜对为止,最后显示用户猜数字的次数后退出程序

import random
x = random.randrange(101)  # 0~100之间
# print(x)

count = 0  # 记录次数
while True:
    y = int(input("请输入整数: "))
    count += 1
    if x == y:
        print("恭喜您猜对了")
        break
    elif y > x:
        print("您猜大了")
    else:
        print("您猜小了")

print("您共猜了%d次" % count)


