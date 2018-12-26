#   1. 写程序.输入一个开始的整数值用begin绑定
#     输入一个结束的整数用end绑定
#       将从begin开始到end结束(不包含end)的所有偶数存于列表中,并打印(建议用列表推导式完成)

begin = int(input("请输入开始值: "))
end = int(input("请输入结束值: "))
L = [x for x in range(begin, end)
        if x % 2 == 0]

print(L)

