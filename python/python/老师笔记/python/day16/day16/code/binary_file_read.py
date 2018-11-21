# binary_file_read.py

# 此示例示意用二进制模式读取文件中的数据
f = open("mynote.txt", 'rb')  # 二进制读

b = f.read()  # 返回字节串
print('读取的内容长度是:', len(b))
print("内容是:", b)
s = b.decode()
print("转为字符串后s为:", s)
f.close()

