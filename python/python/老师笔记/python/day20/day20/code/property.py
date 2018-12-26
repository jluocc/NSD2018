# property.py

# 此示例示意用@property 来实现getter和 setter

class Student:
    def __init__(self, s):
        self.__score = s  # 成绩

    def get_score(self):
        '''getter'''
        return self.__score

    def set_score(self, s):
        '''setter'''
        assert 0 <= s <= 100, "成绩超出范围"
        self.__score = s

s1 = Student(59)
print(s1.get_score())
# print(s1.score)  # 取值
s1.set_score(999999999999)
# s1.score = 999999999999   # 赋值


