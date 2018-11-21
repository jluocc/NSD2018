# inherit2.py

class Human(object):
    '''此类用于描述人类的共性'''
    def say(self, what):
        print("say:", what)

    def walk(self, distance):
        print("走了", distance, "公里")

class Student(Human):
    def study(self, subject):
        print("正在学习:", subject)

class Teacher(Student):
    def teach(self, subject):
        print("正在教:", subject)

h1 = Human()
h1.say("天真蓝")
h1.walk(5)

s1 = Student()
s1.say("学习有点累")
s1.walk(1)
s1.study("Python")

t1 = Teacher()
t1.teach("继承/派生")
t1.say("终于要放假了")
t1.walk(3)
t1.study("转魔方")



