# file_write.py


# 此示例示意写文本文件
try:
    f = open("myfile.txt", 'a')
    print("打开文件成功")

    # 2. 写文件
    f.write("ABCD\n")
    print("写文件成功")

    # 3. 关闭文件
    f.close()
    print("文件已关闭")
except OSError:
    print("打开文件失败")