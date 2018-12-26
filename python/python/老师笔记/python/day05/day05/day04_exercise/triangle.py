# 3. 输入一个整数表示三角形的宽度和高度,打印出如下的三角形:
# 如:
#     请输入三解形的宽度: 4
# 打印如下:
#     *
#     **
#     ***
#     ****

n = int(input("请输入一个三角形的高度: "))

line_number = 1
while line_number <= n:
    # print("第", line_number, '行')
    print("*" * line_number)
    line_number += 1
    