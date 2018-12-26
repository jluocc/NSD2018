# 练习:
#   1. 写程序实现复制文件功能:
#      要求:
#        1. 源文件路径和目标文件路径需手动输入
#        2. 要考虑关闭文件问题
#        3. 要考虑复制超大文件问题
#        4. 要能复制二进制文件


def mycopy(src_file, dst_file):
    """此函数的功以实现复制文件
    src_file : 源文件名
    dst_file : 目标文件名
    """
    try:
        fr = open(src_file, "rb")  # fr读文件
        try:
            try:
                fw = open(dst_file, 'wb')  # fw写文件
                try:
                    while True:
                        data = fr.read(4096)
                        if not data:
                            break
                        fw.write(data)
                except:
                    print("可能U盘被拔出...")
                finally:
                    fw.close()  # 关闭写文件
            except OSError:
                print("打开写文件失败")
                return False
        finally:
            fr.close()  # 关闭读文件
    except OSError:
        print("打开读文件失败")
        return False
    return True

s = input("请输入源文件路径名: ")
d = input("请输入目标文件路径名: ")
if mycopy(s, d):
    print("复制文件成功")
else:
    print("复制文件失败")