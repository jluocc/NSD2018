# mymod2.py


# 此示例示意模块内的__all__列表的定义方式和作用

# 限制 别人用 from import *语句导入时,只能导入: f3 var1
__all__ = ['f3', 'var1']

def f1():
    pass

def f2():
    f1()

def f3():
    f2()

var1 = "aaaa"
var2 = 'bbbb'
