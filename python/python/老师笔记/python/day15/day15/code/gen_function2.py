# gen_function.py


# 此示例示意生成器函数的调用顺序
def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print("生成器函数调用结束")

gen = myyield()
it = iter(gen) #拿到迭代器时,生成不函数不执行
print(next(it))  # 即将生成2  , 2
print(next(it))  # 3
print(next(it))  # 5
print(next(it))  # 7

    
