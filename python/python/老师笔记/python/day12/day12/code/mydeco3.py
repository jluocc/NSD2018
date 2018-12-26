# mydeco2.py

# 此示例用装饰器改变原来函数的调用流程(业务流程)
# 银行业务

# 小铭同学
# 此装饰器用来增加权限验证功能
def privileged_check(fn):
    def fx(n, x):
        print("正在进行权限验证....")
        fn(n, x)
    return fx

# 此装饰器用来增加短消息提醒功能
def message_send(fn):
    def fy(n, x):
        fn(n, x)
        print("正在发送短消息给", n, '...')
    return fy

# -------以下是魏老师写的程序------
@privileged_check
def save_money(name, x):
    print(name, '存钱', x, '元')

@message_send
@privileged_check
def withdraw(name, x):
    print(name, '取钱', x, '元')

# -------以下是小张写的程序------
save_money('小王', 200)
save_money('小赵', 400)
withdraw('小李', 500)




