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

print("%20s" % a)
print("%20s" % b)
print("%20s" % c)



