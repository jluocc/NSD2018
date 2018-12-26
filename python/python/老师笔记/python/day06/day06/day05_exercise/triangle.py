# 练习:
#   1. 写程序输入一个三角形的宽和高,打印相应的三角形:
#     如:
#       输入: 3
#     1) 
#       *
#       **
#       ***
#     2)
#         *
#        **
#       ***
#     3)
#       ***
#       **
#       *
#     4)
#       ***
#        **
#         *


n = int(input("请输入三角形的高: "))
# 1) 
#   *
#   **
#   ***

# stars代表星号个数
for stars in range(1, n+1):
    print("*" * stars)

print("-----------------------")
# 2)
#     *
#    **
#   ***
for stars in range(1, n+1):
    blanks = n - stars  # 计算空格个数
    print(' ' * blanks + "*" * stars)

print('=====================')
# 3)
#   ***
#   **
#   *
for stars in range(n, 0, -1):
    print("*" * stars)

print('++++++++++++++++++++')
# 4)
#   ***
#    **
#     *
for stars in range(n, 0, -1):
    blanks = n - stars
    print(' ' * blanks + "*" * stars)
