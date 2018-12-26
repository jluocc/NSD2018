# constructor.py


class Dog:
    '''此语句用来定义一个新的类型 Dog'''
    pass


dog1 = Dog()  # 创建一个实例对象
print(id(dog1))
dog2 = Dog() # 创建 第二个实例对象
print(id(dog2))

lst1 = list()  # 创建一个列表对象
print(id(lst1))
lst2 = list()  # 创建第二个实例对象
print(id(lst2))

