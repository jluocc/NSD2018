#   3. 给出一个整数n,写一个函数来计算n!(n的阶乘))
#       n! = 1*2*3*4*...*n
#       def myfac(n):
#           ...
#       print(myfac(5))  # 120
  
def myfac(n):
    s = 1
    for x in range(1, n + 1):
        s *= x
    return s


print(myfac(5))  # 120
