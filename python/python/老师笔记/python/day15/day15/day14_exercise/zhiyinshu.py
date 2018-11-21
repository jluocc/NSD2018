#   2. 分解质因数, 输入一个正整数,分解质因数.
#   如输入 : 90  则打印: 90 = 2*3*3*5
#   (质因数是指最小能被原数整除的素数(不包括1))

def get_zhiyin_list(x):
    """此函数将返回包含x的所有质数数的列表
    如:x = 90
    则返回 [2, 3, 3, 5]
    """
    L = []
    # 循环查找x的质数,如果找到质数入就加入到L列表中,直到x等于1为止
    while x > 1:
        # 以下循环只找一个质因数,找以后循环停止
        # 再返回上面的循环
        for i in range(2, x + 1):
            if x % i == 0: # 整除了一定
                # 此时i一定是质因数
                L.append(i)
                x = int(x / i)
                break

    return L


n = int(input("请输入一个大于零的整数: "))
L = get_zhiyin_list(n)
s = '*'.join( (str(x) for x in L) )
print(n, '=', s)

