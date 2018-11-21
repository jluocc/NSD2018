#   4. 改写之前的学生信息管理程序:
#      改为用两个函数实现
#        1)写函数input_student() 来获取学生信息,当输入姓名为空时结束输入.形成字典组成的列表并返回
#        2) 写函数print_student(L) 将上述函数得到的打印成为表格显示
#     如:
#       def input_student():
#           ...
#       def print_student(L):
#           ... 
#       L = input_student()  # 获取列表
#       print(L)
#       print_student(L)  # 打印表格


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


L = input_student()  # 获取列表
print(L)
print_student(L)  # 打印表格
