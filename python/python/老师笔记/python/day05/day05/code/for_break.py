
# 3. for语句中用break语句中断执行时,else子句不会执行

for x in range(10):
    print(x)
    if x == 3:
        break
else:
    print("for语句结束")
