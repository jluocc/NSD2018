# 2. 分三次输入当前的小时，分钟，秒数
# 在终端打印出距离 0:0:0过了多少秒?

hour = input("请输入小时: ")
hour = int(hour)

minute = int(input("请输入分钟: "))
second = int(input("请输入秒数: "))

total_second = (hour * 60 * 60 + minute
 * 60 + second)
print("距离0:0:0过了", total_second, '秒')

