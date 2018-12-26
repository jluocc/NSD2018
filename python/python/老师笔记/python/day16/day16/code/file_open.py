# file_open.py


# 此示例示意文件的打开操作

# 打开文件
try:
    # f = open("mynote.txt")  # 打开文件,用f绑定文件流对象
    f = open("不存在的文件.txt")
    print("成功打开文件")

    # 读写文件

    # 关闭文件
    f.close()
    print("成功关闭文件")
except OSError:
    print("打开文件失败")
