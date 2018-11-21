# 练习:
#   输入三行文字，让这三行文字依次以20个字符的宽度右对齐输出
#   如:
#     请输入第1行: hello beijing
#     请输入第2行: abcd
#     请输入第3行: a
#   输出结果:
#          hello beijing
#                   abcd
#                      a
#   做完上面的题后再思考:
#     能否以最长字符串的长度进行右对齐显示(左侧填充空格)

a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")

# 以最长字符串的长度进行右对齐显示(左侧填充空格)
# 求出最长的字符串长度用变量max_len绑定
# 手动求最长
# max_len = len(a)
# if len(b) > max_len:
#     max_len = len(b)
# if len(c) > max_len:
#     max_len = len(c)

max_len = max(len(a), len(b), len(c))

# 方法1
# print(" " * (max_len - len(a)) + a)
# print(" " * (max_len - len(b)) + b)
# print(" " * (max_len - len(c)) + c)

# 方法2
fmt = "%"  + str(max_len) + "s"
# print("fmt=", fmt)
print(fmt % a)
print(fmt % b)
print(fmt % c)




