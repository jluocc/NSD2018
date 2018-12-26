
# 2. 写程序,让用户输入很多个整数(包含正整数和负整数) 保存于列表L 中. 输入0结束输入. 然后把列表L中的所有正数存于列表L1 中,把列表L中的所有负数存于列表L2中
#   打印原列表L和 正数列表L1 和负数列表L2

L = []
while True:
    x = int(input("请输入整数(0结束): "))
    if x == 0:
        break
    L.append(x)

L1 = [x for x in L if x > 0]  # 正数
L2 = [x for x in L if x < 0]  # 负数
print("原列表是:", L)
print("正数的列表L1=", L1)
print("负数的列表L2=", L2)

