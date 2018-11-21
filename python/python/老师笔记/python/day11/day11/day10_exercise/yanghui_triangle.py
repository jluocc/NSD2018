#   5. 写程序打印杨辉三解(只打印6层)
#          1
#         1 1 
#        1 2 1 
#       1 3 3 1 
#      1 4 6 4 1 
#     1 5 10 10 5 1 

# 第一步,制造相应的列表
def get_next_list(L):
    # 用给定的一行L ,返回下一行
    # 如L为[1, 2, 1] 则返回 [1, 3, 3, 1]
    rl = [1]  # 最左边的1
    # 算中间的数字(循环获取从0开始的索引)
    for i in range(len(L) - 1):
        v = L[i] + L[i + 1]
        rl.append(v)

    rl.append(1)  # 最右边的1
    return rl

# 第二步,生成全部的行放到一个整体的列表rl中,并返回
def yh_list(n):  # n为行数
    # 如果 n为3 最终返回的列表是:
    # [[1],[1, 1], [1, 2, 1]]
    rl = []
    L = [1]
    while len(rl) < n:
        rl.append(L) # 加入当前行
        # 计算出下一行准备加入
        L = get_next_list(L)

    return rl

# 第三步,把杨辉三解的列表转为字符串列表
# 如果给定的列表是[[1], [1, 1], [1, 2, 1]]
# 返回 ['1', '1 1', '1 2 1']
def get_yh_string(L):
    rl = []
    for line in L:
        # line = [1, 2, 1] -> s = '1 2 1'
        str_lst = [str(x) for x in line]
        # str_lst = ['1', '2', '1']
        s = ' '.join(str_lst)
        rl.append(s)
    return rl

# 打印杨辉三解
def print_yh_triangle(L):
    # L = ['1', '1 1', '1 2 1']
    max_len = len(L[-1])
    for s in L:
        print(s.center(max_len))


L = yh_list(10)
SL = get_yh_string(L)
print_yh_triangle(SL)


