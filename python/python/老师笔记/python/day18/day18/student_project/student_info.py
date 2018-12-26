# 2. 改写之前的学生信息管理系统
# 要求添加四个功能:
#     | 5)  按学生成绩高-低显示学生信息 |
#     | 6)  按学生成绩低-高显示学生信息 |
#     | 7)  按学生年龄高-低显示学生信息 |
#     | 8)  按学生年龄低-高显示学生信息 |


def input_student():
    L = []

    while True:
        n = input("请输入姓名: ")
        if not n:
            break
        # 让用户输入年龄,如果输错就重新输入
        # 如果没有错,则跳出循环,做后面后事
        while True:
            try:
                a =int(input("请输入年龄: "))
            except:
                continue
            else:
                break
        try:
            s = int(input("请输入成绩: "))
        except ValueError:
            print("您的输入有误,请重新输入")
            continue
        d = {}
        d['name'] = n
        d['age'] = a
        d['score'] = s
        L.append(d)
    return L

def print_student(L):
    print("+---------------+-----------+----------+")
    print("|     name      |    age    |  score   |")
    print("+---------------+-----------+----------+")

    for d in L:
        line = '|' + d['name'].center(15)
        line += '|' + str(d['age']).center(11)
        line += '|' + str(d['score']).center(10)
        line += '|'
        print(line)

    print("+---------------+-----------+----------+")


def remove_student(L):
    n = input("请输入删除学生的姓名:")
    for i, d in enumerate(L):
        if d['name'] == n:
            del L[i]
            print("删除成功")
            return


def modify_score(L):
    # n = input("请输入学生的姓名:")
    # s = input("请输入学生的成绩:")
    # d = L[-1]
    # d['score'] = 60
    pass

def print_score_desc(L):
    def get_score(d):  # d为字典
        return d['score']
    # 得到排序后的列表
    lst = sorted(L, key=get_score, reverse=True)
    print_student(lst)

def print_score_asc(L):
    lst = sorted(L,
                 key=lambda d:d['score']
                 )
    print_student(lst)

def print_age_desc(L):
    lst = sorted(L,
                 key=lambda d:d['age'],
                 reverse=True
                 )
    print_student(lst)

def print_age_asc(L):
    lst = sorted(L,
                 key=lambda d:d['age']
                 )
    print_student(lst)


def read_from_file():
    L = []
    try:
        f = open("si.txt", 'r')
        for line in f:
            line = line.strip() #去掉'\n'
            items = line.split(',')
            n, a, s = items
            a = int(a)  # 转为整数
            s = int(s)
            L.append(dict(name=n,
                          age=a,
                          score=s))
        f.close()
        print('读取文件成功')
    except OSError:
        print("读取文件失败")

    return L

def save_to_file(L):
    try:
        f = open("si.txt", 'w')
        for d in L:
            f.write(d['name'])
            f.write(',')
            f.write(str(d['age']))
            f.write(',')
            f.write(str(d['score']))
            f.write('\n')
        f.close()
        print("保存成功")
    except OSError:
        print("保存文件失败")



