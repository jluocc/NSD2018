# continue3.py


# 此示例示意将continue用于while循环中的情况
# 用while语句打印 10以内的偶数
i = 0
while i < 10:
    if i % 2 == 1:
        i += 1
        continue
    print(i)
    i += 1