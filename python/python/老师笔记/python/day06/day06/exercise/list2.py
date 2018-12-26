# 1. 输入三个数,存于列表中,打印出这三个数的最大值,最小值和平均值

a = int(input("请输入第1个数: "))
b = int(input("请输入第2个数: "))
c = int(input("请输入第3个数: "))

L = [a, b, c]
print("最大值是:", max(L))
print("最小值是:", min(L))
print("平均值是:", sum(L)/len(L))









