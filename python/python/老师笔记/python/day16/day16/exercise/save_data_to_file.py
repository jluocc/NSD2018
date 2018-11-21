#   1.写一个程序,输入很多人的姓名,年龄,家庭住址,保存在文件"infos.txt"中
#     (格式自定义,建议用空格或逗号分隔符)
#   如: info.txt
#     小李 20 北京市朝阳区
#     小张 18 上海市浦东新区

def get_infos():
    '''此函数返回字典组成的列表
    return [{'name': '小李', 'age': 20, 'address': '北京市朝阳区'},
    {'name': '小张', 'age': 18, 'address': '上海市浦东新区'},
    ]
    '''
    L = []
    while True:
        n = input("请输入姓名: ")
        if not n:
            break
        a = int(input("请输入年龄: "))
        addr = input('请输入家庭住址: ')
        L.append(dict(name=n,
                      age=a,
                      address=addr))
    return L

def save_to_file(L):
    try:
        # 打开文件
        f = open("infos.txt", 'w')
        for d in L:
            f.write(d['name'])
            f.write(' ')
            f.write(str(d['age']))  # 需要转为字符串
            f.write(' ')
            f.write(d['address'])
            f.write('\n')  # 输出换行

        f.close()
    except OSError:
        print('打开文件失败')

# 分两步来做:
# 1. 读取数据形成字典组成的列表
L = get_infos()
# 2. 把列表里的数据保存到文件infos.txt中
print(L)
save_to_file(L)
