# 1. 用for语句打印 1～20的整数，打印在一行内.
for x in range(1, 21):
    print(x, end=' ')
print()

# 2. 用for语句打印 1～20的整数，每行打印5个,打印4行.
for x in range(1, 21):
    print(x, end=' ')
    if x % 5 == 0:
        print()
print()
