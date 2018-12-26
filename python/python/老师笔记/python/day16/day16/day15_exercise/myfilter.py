#   3. 写一个myfilter生成器函数,功能与filter函数功能完全相同
#      如:
#         def myfilter(fn, iter1):
#              ...
#         L = [x for x in myfilter(
#             lambda x: x%2, range(10)
#         )]  # L = [1, 3, 5, 7, 9]


def myfilter(fn, iter1):
    for x in iter1:
        if fn(x) == True:
            yield x


L = [x for x in myfilter(
    lambda x: x%2, range(10)
)]  # L = [1, 3, 5, 7, 9]

print(L)