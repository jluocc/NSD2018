
# 用生成器函数实现myzip函数


numbers = [10086, 10000, 10010,95588]
names = ['中国移动','中国电信','中国联通']

# def myzip(*args):
def myzip(iter1, iter2):
    # 先拿到两个对象的迭代器
    it1 = iter(iter1)
    it2 = iter(iter2)
    while True:
        try:
            a = next(it1)
            b = next(it2)
            yield (a, b)
        except StopIteration:
            return  # 此生成器函数生成结束

for t in myzip(numbers, names):
    print(t)

d = dict(myzip(numbers, names))
print(d)
