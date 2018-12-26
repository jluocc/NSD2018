# with.py
try:
    # 用with语句实现
    # f = open("text.txt", 'w')
    with open("text.txt", 'w') as f:
        s = int(input("请输入整数:"))  #故意制造异常

        f.write("hello")
except OSError:
    print("文件打开失败")
except: 
    print("写入数据失败")
