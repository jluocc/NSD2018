# iterator.py

L = [2, 3, 5, 7]
it = iter(L)  # 获取迭代器
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

print("--------------------")
for x in L:
    print(x)



