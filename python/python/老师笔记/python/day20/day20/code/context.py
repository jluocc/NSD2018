# context.py

# 此示例示意自定义用 with 管理的对象
class A:
    '''此类的对象将可用于with语句中'''
    def __enter__(self):
        print("已经进入到了with语句的内部")
        return self  #把自己返回由as 来绑定
    def __exit__(self, e_t, e_v, e_tb):
        ''' e_t 用来绑定异常类型
            e_v用来绑定异常对象
            e_tb_用来绑定追踪对象
            在没有异常时,三个形参都绑定None
        '''
        if e_t is None:
            print("已正常离开with语句")
        else:
            print("是在出现异常时走异常流程离开的with语句")

with A() as a:
    print('这是with语句内部的print')
    int(input("请输入整数: "))
