# seek.py

# 此示例示意用seek 来改动文件的读写位置 

f = open('data.txt', 'rb')
b = f.read(3)
print("您读取的是:", b)
print("当前的读写位置是:", f.tell())

# 以下读写第5至第10个字节的b'abcde'
# f.seek(5, 0)  # 从文件头开始向后移动5个字节
# f.seek(2, 1)  # 从当前位置向后移动2个字节
f.seek(-15, 2)  # 从文件尾向向前移动15个字节

print("当前的读写位置是: ", f.tell())
b = f.read(5)
print("读取的内容是:", b)

f.close()






