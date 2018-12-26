# 练习:
#   写一个函数get_age() 用来获取一个人的年龄信息
#   此函数规定用户只能输入1~140之间的整数,如果用户输入的数是其它的数值,则直接触发ValueError类型的错误!
#   如 : 
#     def get_age():
#         ...
    
#     try:
#         age = get_age()
#         print("用户输入的年龄是", age)
#     except ValueError as err:
#         print("用户输入的不是1~140的数字,获取年龄失败")


def get_age():
    try:
        a = int(input("请输入年龄: "))
    except ValueError:
        raise ValueError("用户输入的不是数字")
    if a < 1:
        raise ValueError("用户输入的年龄太小")
    if a > 140:
        raise ValueError("用户输入的年龄太大")
    return a
try:
    age = get_age()
    print("用户输入的年龄是", age)
except ValueError as err:
    print("用户输入的不是1~140的数字,获取年龄失败")
    print("err=", err)
