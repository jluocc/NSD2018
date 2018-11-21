# pass.py

# 让用户输入一个学生成绩(0~100)之间,判断是否为有效成绩
x = int(input("请输入成绩:"))

if 0 <= x <= 100:
    pass
else:
    print("输入成绩不合法")

if not (0 <= x <= 100):
    print("输入成绩不合法")

