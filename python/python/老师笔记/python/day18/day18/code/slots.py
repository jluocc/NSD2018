# slots.py

# 此示例示意类内的__slots__列表的用法
class Human:
    # 限制Human类的对象只能有"name", 和"age"属性,不能有其它属性
    __slots__ = ['name', 'age']
    def __init__(self, n, a):
        self.name, self.age = n, a
    def show_info(self):
        print(self.name, self.age)

s1 = Human("Tarena", 15)
s1.show_info()  # ????
s1.Age = 16  # 报错
s1.show_info()  # ????




