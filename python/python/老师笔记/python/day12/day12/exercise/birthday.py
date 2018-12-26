# 练习:
#   写一个程序,输入你的生日
#     1) 算出你已经出生多少天?
#     2) 算出你出生那天是星期几?
import time

y = int(input("请输入出生时的年: "))
m = int(input("请输入出生时的月: "))
d = int(input("请输入出生时的日: "))
# 先得到出生时的时间元组
t = (y, m, d, 0, 0, 0, 0, 0, 0)

# 再得到出生时间的秒数(UTC秒数)
birth_second = time.mktime(t)

# 得到当前时间秒数(UTC秒数)
cur_second = time.time()

# 出生时间秒数
life_second = cur_second - birth_second

print("您已出生",
      life_second/60/60//24,
      '天')

# 用出生时间的UTC秒数转为本地时间:
t = time.localtime(birth_second)
# print(t)
d = {
    0: '一',
    1: '二',
    2: '三',
    3: '四',
    4: '五',
    5: '六',
    6: '日'
}
print("您出生的那天是星期", d[t[6]])
