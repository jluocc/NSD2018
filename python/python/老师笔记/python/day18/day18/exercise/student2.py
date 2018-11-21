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
    infos = []
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    @classmethod
    def input_student(cls):
        while True:
            n = input("请输入姓名: ")
            if not n:
                break
            a = int(input("请输入年龄: "))
            s = int(input("请输入成绩: "))
            cls.infos.append(Student(n, a, s))

    @classmethod
    def del_student(cls):
        n = input("请输入要删除学生的姓名: ")
        for index, s in enumerate(cls.infos):
            if s.name == n:
                del cls.infos[index]
                return

    @classmethod
    def print_student_count(cls):
        '1) 打印出学生的个数'
        print("学生个数是:", len(cls.infos))

    @classmethod
    def print_avg_score(cls):
        '2) 打印出所有学生的平均成绩'
        total_score = 0
        for s in cls.infos:
            total_score += s.score
        # total_score = sum((s.score for s in L))

        print("平均成绩是:", total_score/len(cls.infos))

    @classmethod
    def output_student(cls):
        for s in cls.infos:
            print(s.name, s.age, s.score)
#  3) 打印出所有学生的平均年龄
#   (建议用列表的长度来计算学生的个数)

Student.input_student()
Student.output_student()
Student.del_student()
Student.output_student()
Student.print_student_count()
Student.print_avg_score()


