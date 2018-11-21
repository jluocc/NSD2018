
def myinput(fn):
    L = [1, 3, 5, 7, 9]
    r = fn(L)
    return r

print(myinput(max))  # 9
print(myinput(min))  # 1
print(myinput(sum))  # 25

