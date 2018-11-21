# mydeco2.py

# 此示例用装饰器改变原来函数的调用流程(业务流程)
# 银行业务

# 小铭同学
def privileged_check(fn):
    def fx(n, x):
        print("正在进行权限验证....")
        fn(n, x)
    return fx

# -------以下是魏老师写的程序------
@privileged_check
def save_money(name, x):
    print(name, '存钱', x, '元')

@privileged_check
def withdraw(name, x):
    print(name, '取钱', x, '元')

# -------以下是小张写的程序------
save_money('小王', 200)
save_money('小赵', 400)
withdraw('小李', 500)




