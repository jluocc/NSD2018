
# 此示例示意raise 无参用法

def fa():
    print("---fa---开始")
    raise ValueError("故意制造的一个错误!")
    # int("aaaa")
    print("---fa---结束")

def fb():
    print("fb开始")
    try:
        fa()
    except ValueError as err:
        print("fa里发生了值错误已处理")
        # 此处如果要将err再次向上传递
        raise
    print("fb结束")

try:
    fb()
except ValueError:
    print("再一次收到fb内部发生的错误 ")




