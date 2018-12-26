# try-except.py

# 此示例示意try-except 语句的基本语法和用法
import os
def div_apple(n):
    print("有%d个苹果,您想分给几个人?" % n)
    s = input("请输入人数: ")
    count = int(s)  #可能触发ValueError错误
    result = n / count #ZeroDivisionError
    print("每个人分了%d个苹果" % result)

try:
    div_apple(10)
except ValueError:
    print("分苹果时发生值错误异常,已捕获并转为正常状态")
    print("把苹果拿回来")
except ZeroDivisionError:
    print("没有人来拿苹果,苹果被收回")

print("程序正常结束")







