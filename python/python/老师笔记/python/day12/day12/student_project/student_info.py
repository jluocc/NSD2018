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
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
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
    # n = input("请输入删除学生的姓名:")
    # 删除最后一个学生:
    # del L[-1]
    pass

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



def show_menu():
    print("+--------------------------------+")
    print("| 1) 添加学生信息                |")
    print("| 2) 显示学生信息                |")
    print("| 3) 删除学生信息                |")
    print("| 4) 修改学生成绩                |")
    print("| 5) 按学生成绩高-低显示学生信息 |")
    print("| 6) 按学生成绩低-高显示学生信息 |")
    print("| 7) 按学生年龄高-低显示学生信息 |")
    print("| 8) 按学生年龄低-高显示学生信息 |")
    print("| q) 退出                        |")
    print("+--------------------------------+")




def main():
    infos = []  # 用于保存学生信息的列表
    while True:
        # 打印菜单:
        show_menu()
        s = input('请选择: ')
        if s == '1':
            infos += input_student()
        elif s == '2':
            print_student(infos)
        elif s == '3':
            remove_student(infos)
        elif s == '4':
            modify_score(infos)
        elif s == '5':
            #5)  按学生成绩高-低显示学生信息
            print_score_desc(infos)
        elif s == '6':
            #6)  按学生成绩低-高显示学生信息
            print_score_asc(infos)
        elif s == '7':
            #7)  按学生年龄高-低显示学生信息
            print_age_desc(infos)
        elif s == '8':
            #8)  按学生年龄低-高显示学生信息
            print_age_asc(infos)
        elif s == 'q':
            break


main()