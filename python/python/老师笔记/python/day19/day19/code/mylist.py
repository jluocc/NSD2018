# mylist.py

class MyList:
    '''创建一个自定义列表类,
    此MyList内部用列表来存储信息'''
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __len__(self):
        '''方法必须反回整数'''
        return self.data.__len__()
        # return len(self.data)

    def __abs__(self):
        '''此方法实现把self的所有元素取绝对
        值后返回全为正数的自定义列表MyList'''
        lst = [abs(x) for x in self.data]
        L = MyList(lst)  # 创建新的MyList
        return L

myl = MyList([1, -2, 3, -4])
print(myl)
print("myl 的长度是:", len(myl))  # myl.__len__()

myL3 = abs(myl)
print(myL3)  # MyList([1, 2, 3, 4])


# myl2 = MyList()
# print(myl2)

