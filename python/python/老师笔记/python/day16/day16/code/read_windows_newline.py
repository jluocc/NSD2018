

f = open("mynote_windows.txt")
s  = f.read()
print("s=", s)
print(len(s))  # 7字符('\r\n'已自动转换为'\n')