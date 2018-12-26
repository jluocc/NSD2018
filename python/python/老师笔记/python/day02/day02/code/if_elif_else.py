# if_elif_else.py


# 此示例示意if-elif 语句的用法
# 输入一个整数，判断这个数是正数，负数，零
num = int(input("请输入一个整数:"))
if num > 0:
    print(num, '是正数')
elif num < 0:
    print(num, '是负数')
# elif num == 0:
else:
    print(num, '是零')

print("程序结束")