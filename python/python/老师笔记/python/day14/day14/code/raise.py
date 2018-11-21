# raise.py

# 此示例示意raise 发送错误通知的用法
def make_except():
    print("函数开始")

    # 发出ZeroDivisionError类型的错误给调用者
    # raise ZeroDivisionError
    # raise ValueError
    e = ValueError("值错误")  #创建一个错误对象
    raise e

    print("函数结束")

try:
    make_except()
except ZeroDivisionError:
    print("接收到make_except发出的错误通知")
except ValueError as err:
    print("ValueError--->", err)

print("程序正常结束")
