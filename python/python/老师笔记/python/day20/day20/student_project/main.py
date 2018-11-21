# file : main.py
# 学生管理系统的主模块

from menu import show_menu
from student_info import *

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
        elif s == '9':
            infos = read_from_file()
        elif s == '10':
            save_to_file(infos)
        elif s == 'q':
            break


main()