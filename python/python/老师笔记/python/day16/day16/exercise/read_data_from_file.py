#   2. 写一个程序,读入infos.txt中的内容,以如下格式打印:
#     姓名: 小张, 年龄:20, 住址: 北京市朝阳区
#     ...

def read_from_file():
    '''返回字典组成的列表'''
    L = []
    try:
        f = open("infos.txt", 'r')
        while True:
            line = f.readline()
            if not line:
                break
            line = line.rstrip()  #'\n'
            items = line.split() 
            d = dict(name=items[0],
                    age=int(items[1]), 
                    address = items[2]
                    )
            L.append(d)
        f.close()
        print("读取文件成功")
    except OSError:
        print("打开文件失败")
    return L

def print_infos(L):
    print(L)  # 打印列表中的数据

# 分两步:
# 1. 从文件中读取数据,形成字典组成的列表
L = read_from_file()
# 2. 打印列表中的数据
print_infos(L)



