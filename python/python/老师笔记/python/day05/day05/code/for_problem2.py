# 2. for语句变量列表里的变量可能不被创建


for x in range(4, 0):
    print(x)
else:
    print("循环结束后x的值是", x)  # 报错
