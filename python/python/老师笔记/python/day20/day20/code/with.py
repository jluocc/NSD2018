# with.py
try:
    f = open("text.txt", 'w')
    try:
        s = int(input("请输入整数:"))  #故意制造异常

        f.write("hello")
    finally:
        f.close()
except OSError:
    print("文件打开失败")
except: 
    print("读取数据失败")
