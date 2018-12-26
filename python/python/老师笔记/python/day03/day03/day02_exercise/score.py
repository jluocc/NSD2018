# 2. 输入一个学生的三科成绩:
# 打印出最高分是多少?
# 打印出最低分是多少?
# 打印出平均分是多少?

a = int(input("请输入第1科成绩: "))
b = int(input("请输入第2科成绩: "))
c = int(input("请输入第3科成绩: "))

# 方法1
# if a > b:
#     # a比较大
#     if a > c:
#         zuida = a
#     else:
#         zuida = c
# else:
#     # b比较大
#     if b > c:
#         zuida = b
#     else:
#         zuida = c

# 方法1
zuida = a
if b > zuida:
    zuida = b

if c > zuida:
    zuida = c

print("最大值是:", zuida)

