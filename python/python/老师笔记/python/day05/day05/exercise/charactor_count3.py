# 练习:
#   任意输入一段字符串
#     1) 计算这个字符串中'a' 这个字符的个数,并打印出来
#     2) 计算出空格的个数，并打印出来
#     (要求: 用for语句实现，不允许使用 S.count方法)
# 　思考:
#     用while语句能否实现上述功能?

s = input("请输一段文字: ")  

count_a = 0  # 此变量用来记录a的个数
count_blank = 0  # 此变量用来记录空格的个数
# for ch in s:
#     if ch == 'a':
#         count_a += 1
#     if ch == ' ':
#         count_blank += 1
i = 0  # i代表索引值
while i < len(s):
    ch = s[i]
    if ch == 'a':
        count_a += 1
    if ch == ' ':
        count_blank += 1
    i += 1

print("'a'这个字符的个数是:", count_a)
print("空格的个数是:", count_blank)
