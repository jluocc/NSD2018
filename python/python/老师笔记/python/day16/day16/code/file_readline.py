# file_readline.py


# 此示例示意文件的打开和读操作

try:
    # 打开文件
    f = open("/home/tarena/aid1808/pbase/day16/code/mynote.txt")

    # 读写文件
    s = f.readline()  # 从文件中读取一行文字
    print("您读到的是:", s)
    print("您读取的字符个数得:", len(s))

    # 关闭文件
    f.close()
    print("成功关闭文件")
except OSError:
    print("打开文件失败")




