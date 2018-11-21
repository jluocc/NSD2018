# 1. 用类来描述一个学生的信息(可以修改之前写的Student类)
#   class Student:
#       .... 以下自己实现
#   学生信息有:
#      姓名, 年龄, 成绩
#   将这些学生对象存于列表中,可以任意添加和删除学生信息.
#      1) 打印出学生的个数
#      2) 打印出所有学生的平均成绩
#      3) 打印出所有学生的平均年龄
#       (建议用列表的长度来计算学生的个数)


class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s


infos = []
def input_student():
    L = []
    while True:
        n = input("请输入姓名: ")
        if not n:
            break
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
        L.append(Student(n, a, s))
    return L

def del_student(L):
    n = input("请输入要删除学生的姓名: ")
    for index, s in enumerate(L):
        if s.name == n:
            del L[index]
            return


def print_student_count(L):
    '1) 打印出学生的个数'
    print("学生个数是:", len(L))

def print_avg_score(L):
    '2) 打印出所有学生的平均成绩'
    total_score = 0
    for s in L:
        total_score += s.score
    # total_score = sum((s.score for s in L))

    print("平均成绩是:", total_score/len(L))

#  3) 打印出所有学生的平均年龄
#   (建议用列表的长度来计算学生的个数)


infos += input_student()
print(infos)

del_student(infos)
print(infos)

print_student_count(infos)
print_avg_score(infos)

