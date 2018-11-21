# property.py

# 此示例示意用@property 来实现getter和 setter

class Student:
    def __init__(self, s):
        self.__score = s  # 成绩

    @property
    def score(self):
        '''getter'''
        print("调用getter")
        return self.__score

    @score.setter
    def score(self, s):
        '''setter'''
        print("调用setter")
        assert 0 <= s <= 100, "成绩超出范围"
        self.__score = s

s1 = Student(59)
print(s1.score)  # 取值
# s1.score = 999999999999 #触发AssertionError
s1.score = 80   # 赋值
print(s1.score)

