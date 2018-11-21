#   1. 打印 9 x 9 乘法表:
#     1x1=1
#     1x2=2 2x2=4
#     1x3=3 2x3=6 3x3=9
#     ......
#     1x9=9 ..............   9x9=81

for line in range(1, 10):
    # 每循环一次打印一行
    for col in range(1, line + 1):
        # 打印一个公式
        print("%dx%d=%d " %
              (col, line, col*line),
              end='')
    print() # 一行完成换行

