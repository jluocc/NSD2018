#   2. 写程序.
#     输入一个开始值用begin绑定
#     输入一个结束值用end绑定
#       计算:
#       从begin开始,到end结束的所有整数的和
#     如:
#        请输入开始值: 1
#        请输入结束值: 10
#     打印:
#        和是: 55

begin = int(input("请输入开始值: "))
end = int(input("请输入结束值: "))

s = 0
i = begin
while i <= end:
    s += i
    i += 1

print("和是:", s)