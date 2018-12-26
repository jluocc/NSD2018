# function_embed2.py


# 此示例示意函数嵌套定义
def fn_outter():
    print("fn_outter被调用")
    def fn_inner():
        print("fn_inner被调用")
    fn_inner()  # 调用一次
    fn_inner()  # 调用第二次
    print("fn_outter调用结束!")
    return fn_inner

f = fn_outter()
# fn_inner()  # 不可以
f()  # fn_inner被调用




