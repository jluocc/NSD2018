# 练习:
#   1. 修改原来的学生信息管理程序,将原来用字典存储学生信息改变用学生Student类型的对象来存储信息
#     要求:
#       1. 类 Student 存于文件 student.py中
#       2. 尽量少在类的外部使用实例变量(建议增加实例方法来获取实例变量的信息)

from student import Student

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
        L.append(Student(n, a, s))
    return L

def print_student(L):
    print("+---------------+-----------+----------+")
    print("|     name      |    age    |  score   |")
    print("+---------------+-----------+----------+")

    for d in L:
        n, a, s = d.get_infos_string()
        line = '|' + n.center(15)
        line += '|' + a.center(11)
        line += '|' + s.center(10)
        line += '|'
        print(line)

    print("+---------------+-----------+----------+")


def remove_student(L):
    n = input("请输入删除学生的姓名:")
    for i, d in enumerate(L):
        if d.get_name() == n:
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
        return d.get_score()
    # 得到排序后的列表
    lst = sorted(L, key=get_score, reverse=True)
    print_student(lst)

def print_score_asc(L):
    lst = sorted(L,
                 key=lambda d:d.get_score()
                 )
    print_student(lst)

def print_age_desc(L):
    lst = sorted(L,
                 key=lambda d:d.get_age(),
                 reverse=True
                 )
    print_student(lst)

def print_age_asc(L):
    lst = sorted(L,
                 key=lambda d:d.get_age()
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
            L.append(Student(n, a, s))
        f.close()
        print('读取文件成功')
    except OSError:
        print("读取文件失败")

    return L

def save_to_file(L):
    try:
        f = open("si.txt", 'w')
        for d in L:
            d.write_to_file(f)
        f.close()
        print("保存成功")
    except OSError:
        print("保存文件失败")



