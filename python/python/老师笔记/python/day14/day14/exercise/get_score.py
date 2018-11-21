# 练习:
#   写一个函数 get_score() 来获取学生输入的成绩(0 ~ 100) 的数,如果用户输入的不是0~100的整数则返回0,否则返回输入的整数
#   如:
#     def get_score():
#         ...
#     score = get_score()
#     print("您输入的成绩是:", score)

# 方法1 在调用get_score时加入try语句
def get_score():
    s = int(input("请输入成绩(0~100): "))
    if not (0 <= s <= 100):
        return 0
    return s

try:
    score = get_score()
except ValueError:
    # 如果末获取到学生信息,则此时学生成绩为0
    score = 0
print("您输入的成绩是:", score)

