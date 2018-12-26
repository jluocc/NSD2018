# star_tuple_args.py


# 此示例示意星号元组形参的定义及使用
def func(*args):
    print("用户传入的参数个数是:",len(args))
    print('args=', args)

# func()  # 无参调用
# func(1, 2, 3)
func(1, 2, 3, "AAA", "BBB", "CCC")
