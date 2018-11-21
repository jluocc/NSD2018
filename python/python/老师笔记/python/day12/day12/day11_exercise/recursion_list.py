#   3. 已知有列表:
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写个函数print_list(lst)  打印出所有的数字,即:
#       print_list(L)  # 打印3 5 8 10 13...
#     2) 写一个函数sum_list(lst) 返回这个列表中所有数字的和
#        print(sum_list(L))  # 106
#   注:
#     type(x) 可以返回一个变量的类型,如:
#        >>> type(20) is int  # True
#        >>> type([1, 2, 3]) is list # True



L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# 1) 写个函数print_list(lst)  打印出所有的数字,即:
def print_list(lst):
    for x in lst:
        # 当x是数字时,打印这个数字
        if type(x) is int:
            print(x)
        # 当x是列表时,打印列表
        else:
            print_list(x)

print_list(L)  # 打印3 5 8 10 13...


# 2) 写一个函数sum_list(lst) 返回这个列表中所有数字的和

def sum_list(lst):
    s = 0
    for x in lst:
        # 如果x是整数
        if type(x) is int:
            s += x
        # 如果x是列表,则s+= 列表的所有元素的和
        else:
            s += sum_list(x)

    return s

print(sum_list(L))  # 106

