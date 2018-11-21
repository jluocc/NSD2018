
# 此示例示意用if 语句嵌套来实现下面程序的功能
n = int(input("请输入月份(1~12): "))
if 1 <= n <= 12:
    print("用户输入的是合法的月份")
    if n <= 3:
        print("春季")
    elif n <= 6:
        print("夏季")
    elif n <= 9:
        print("秋季")
    else:
        print("冬季")
else:
    print("您输错了")


# 2. 输入一年中的月份(1~12), 输出这个月在哪儿个季度.如果输入的是其它的数，则提示您输错了

# n = int(input('请输入月份(1～12): '))
# if 1 <= n <= 3:
#     print("春季")
# elif 4 <= n <= 6:
#     print("夏季")
# elif 7 <= n <= 9:
#     print("秋季")
# elif 10 <= n <= 12:
#     print("冬季")
# else:
#     print("您输错了")



