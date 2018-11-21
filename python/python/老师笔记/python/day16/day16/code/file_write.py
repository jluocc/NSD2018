# file_write.py


# 此示例示意写文本文件
try:
    # 1. 打开文件
    # f = open("/myfile.txt", 'w')  # 失败
    f = open("myfile.txt", 'w')
    print("打开文件成功")

    # 2. 写文件
    f.write("这是第一行文字")
    f.write("\n\n")
    f.write("ABCDEFG")
    f.writelines(["aaaaaaaaaa",
                "bbbbbb",
                "cccccc"])

    print("写文件成功")

    # 3. 关闭文件
    f.close()
    print("文件已关闭")
except OSError:
    print("打开文件失败")