# 面向对象综合练习:
#   两个人:
#     1. 姓名: 张三, 年龄: 35
#     2. 姓名: 李四, 年龄: 8
#   行为:
#     教别人学东西 teach
#     赚钱 work
#     借钱 borrow
#     显示自己的信息 show_info

#   事情:
#     张三 教 李四 学 python
#     李四 教 张三 学 王者荣耀
#     张三 上班赚了 1000 元钱
#     李四 向 张三 借了 200 元钱
#     35 岁的 张三 有钱 800 元,它学会的技能是:王者荣耀
#     8 岁的 李四 有钱 200 元,它学会的技能是:python

# 程序如下:
# class Human:
#     ... 以下自己完成

# zhang3 = Human("张三", 35)
# li4 = Human("李四", 8)
# # 张三 教 李四 学 python
# zhang3.teach(li4, "Python")
# # 李四 教 张三 学 王者荣耀
# li4.teach(zhang3, "王者荣耀")
# # 张三 上班赚了 1000 元钱
# zhang3.work(1000)
# # 李四 向 张三 借了 200 元钱
# li4.borrow(zhang3, 200)
# # 35 岁的 张三 有钱 800 元,它学会的技能是:王者荣耀
# zhang3.show_info()
# # 8 岁的 李四 有钱 200 元,它学会的技能是:python
# li4.show_info()


class Human:
    def __init__(self, n, a):
        self.name = n  # 姓名
        self.age = a  # 年龄
        self.money = 0  # 钱数
        self.skill = []  # 技能

    def teach(self, other, skill):
        print(self.name, "教", 
              other.name, skill)
        other.skill.append(skill)

    def work(self, money):
        print(self.name, "上班赚了",
              money, '元钱')
        self.money += money
    
    def borrow(self, other, money):
        if money > other.money:
            print("借钱失败")
        else:
            print(self.name, "向",
                other.name, "借了", 
                money, "元钱")
            other.money -= money
            self.money += money

    def show_info(self):
        print(self.age, "岁的",
              self.name, "有钱", self.money,
              "元,它学会的技能是:",
              self.skill)

zhang3 = Human("张三", 35)
li4 = Human("李四", 8)
# 张三 教 李四 学 python
zhang3.teach(li4, "Python")
# 李四 教 张三 学 王者荣耀
li4.teach(zhang3, "王者荣耀")
# 张三 上班赚了 1000 元钱
# zhang3.work(1000)
# 李四 向 张三 借了 200 元钱
li4.borrow(zhang3, 200)
# 35 岁的 张三 有钱 800 元,它学会的技能是:王者荣耀
zhang3.show_info()
# 8 岁的 李四 有钱 200 元,它学会的技能是:python
li4.show_info()