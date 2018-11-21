# 练习:
#   已知有列表:
#     L = [2, 3, 5, 7, 10, 15]
#   1) 写一个生成器函数,让此函数能动态提供数据,数据为原列表的数字的平方+1
#   2) 写一个生成器表达式,让此表达式能动态提供数据,数据依旧为原列表数字的平方+1
#   3) 生成一个列表,此列表内的数据为原列表的数字的平方+1


L = [2, 3, 5, 7, 10, 15]
#   1) 写一个生成器函数,让此函数能动态提供数据,数据为原列表的数字的平方+1
def mygen_fun(lst):
    for x in lst:
        yield x ** 2 + 1
L2 = list(mygen_fun(L))
print(L2)

# def mygen_fun2():
#     for x in L:
#         yield x ** 2 + 1
# L2 = list(mygen_fun())
# print(L2)


#   2) 写一个生成器表达式,让此表达式能动态提供数据,数据依旧为原列表数字的平方+1

L3 = list( (x ** 2 + 1 for x in L) )
print('L3=', L3)
#   3) 生成一个列表,此列表内的数据为原列表的数字的平方+1

L4 = [x ** 2 + 1 for x in L]
print("L4=", L4)


