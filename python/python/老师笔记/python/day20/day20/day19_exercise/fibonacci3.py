#   3. 写一个类,Fibonacci实现迭代器协议,此类的对象可以作为可迭代对象生成相应的斐波那契数
#     1 1 2 3 5 8 13 ....
#     如:
#         class Fibonacci:
#             def __init__(self, n):
#                 ...
#             ....
#     实现如下操作:
#         for x in Fibonacci(5)
#             print(x)  # 1 1 2 3 5
#         L = [x for x in Fibonacci(50)]
#         print(L)
#         pring(sum(Fibonacci(100)))


class Fibonacci:
    def __init__(self, n):
        self.count = n  # 记录要生成的数据的个数
        self.a = 0
        self.b = 1  # 绑定当前fibonacci数
        self.cur_count = 0  # 记录已经生成了多少个

    def __iter__(self):
        return self  # 迭代器

    def __next__(self):
        '''由迭代器来生成Fibonacci数'''
        if self.cur_count > self.count:
            raise StopIteration  # 生成完毕
        v = self.b  # 要返回值
        # 算出下一个数,放在self.b中
        self.a, self.b = self.b, self.a + self.b
        # 将已生成的数 加1
        self.cur_count += 1
        return v


for x in Fibonacci(5):
    print(x)  # 1 1 2 3 5
L = [x for x in Fibonacci(50)]
print(L)
print(sum(Fibonacci(100)))
