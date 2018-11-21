# lambda.py


# def myadd(x, y):
#     return x + y

# 可以用lambda改写如下:
# myadd = lambda x, y: x + y
myadd = lambda *args : sum(args)

print("20+30=", myadd(20, 30))  # 50
print("100+200=", myadd(100, 200))  # 300


