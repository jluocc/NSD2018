# 练习:
#   写一个程序,打印26个大写英文字母 和 26个小写英文字母
#   ABCDEFG....XYZabcdefg....XYZ

#   chr(i)  数字转为字符
#   "A"  --> 65
#   'a'  --> 97

for code in range(ord('A'), ord('Z') +1):
    print(chr(code), end='')

for code in range(ord('a'), ord('z') +1):
    print(chr(code), end='')

print()  # 换行
for code in range(0, 65536):
    print(chr(code), end='')
