# tell.py

# 此示例示意用F.tell() 方法获取文件流的读写位置
f = open("data.txt", 'rb')

f.read(3)
print("当前的读写位置是:", f.tell())  # 3

f.read(7)
print("当前的读写位置是:", f.tell())  # 10

f.close()
