# 1. 输入一个整数代表开始用begin绑定
#     输入一个整数代表结束用end绑定
#     打印 begin~ end(不包含end) 之间的全部奇数

begin = int(input("请输入开始值: "))
end = int(input("请输入结束值: "))

# 方法1
for x in range(begin, end):
    if x % 2 == 0:
        continue
    print(x)

# 方法2
for x in range(begin, end):
    if x % 2 == 1:
        print(x)

