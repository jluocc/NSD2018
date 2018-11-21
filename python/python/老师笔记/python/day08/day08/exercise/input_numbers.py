#   3. 写一个函数 input_numbers,如下:
#       def input_numbers():
#          ....  # 此处自己实现
#       此函数用来获取用户循环输入的正整数,当用户输入负数时结束输入
#       将用户输入的数字以列表的形式返回,再用内建函数max,min,sum求出用户输入数的最大值,最小值及和

#       L = input_numbers()
#       print(L)  # 打印列表
#       print("用户输入的最大数是:", max(L))
#       print("用户输入的最小数是:", min(L))
#       print("用户输入的数的和是:", sum(L))




def input_numbers():
    lst = []
    while True:
        n = int(input("请输入正整数(负数结束):"))
        if n < 0:
            return lst
            # break  # return lst
        lst.append(n)
    # return lst

L = input_numbers()
print(L)  # 打印列表
print("用户输入的最大数是:", max(L))
print("用户输入的最小数是:", min(L))
print("用户输入的数的和是:", sum(L))

