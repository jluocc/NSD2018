# stdin.py


import sys

# 从标准输入文件中读取内容
# ctrl + d 输入文件结束符
s = sys.stdin.readline()
print(s)
print("len(s)=", len(s))

# 关闭标准输入文件,input将不再可用
# sys.stdin.close()

s = input("请输入: ")
print(s)

