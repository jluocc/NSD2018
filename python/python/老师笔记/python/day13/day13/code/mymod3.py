# mymod3.py

# 此示例示意隐藏属性,在用from mymod3 import *导入时,只能导入 f 和 name1
def f():
    pass

def _f():
    pass

def __f():
    pass

name1 = "aaa"
_name1 = "bbb"