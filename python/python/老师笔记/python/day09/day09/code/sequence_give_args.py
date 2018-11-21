

# 此示例示意序列传参
def myfun1(a, b, c):
    print("a的值是:", a)
    print("b的值是:", b)
    print("c的值是:", c)


s1 = [11, 22, 33]
# myfun1(s1[0], s1[1], s1[2])
myfun1(*s1)  # 相当于 fun1(11, 22, 33)
s2 = (44, 55, 66)
s3 = "ABC"
myfun1(*s2)
myfun1(*s3)







