# 1. 打印从零开始的浮点数,每个数增加0.5,打印出10以内这样的数
#     0.0  0.5  1.0  1.5  ..... 9.0  9.5

f = 0.0
while f < 10:
    print(f, end=' ')
    f += 0.5

print() # 换行
