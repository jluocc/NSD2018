# 2. 写程序,输入三行文字,让这三行文字在一个方框内居中显示
# 如:
#     请输入: hello!
#     请输入: I'm studing python!
#     请输入: I like python!
# 打印如下:
#     +---------------------+
#     |        hello!       |
#     | I'm studing python! |
#     |    I like python!   |
#     +---------------------+
# 注:  不要输入中文

a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")

max_len = max(len(a), len(b), len(c))
# 打印第一行
first_line = "+" + '-' * (max_len + 2) + '+'
print(first_line)

print("| " + a.center(max_len) + ' |')
print("| " + b.center(max_len) + ' |')
print("| " + c.center(max_len) + ' |')

# 打印最后行
print(first_line)
