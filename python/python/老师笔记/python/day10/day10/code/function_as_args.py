# function_as_args.py


def f1():
    print("hello f1")

def f2():
    print("hello f2")

def fx(fn):
    print(fn)  # <function f1 at 0x????>
    fn()   # 请问调用谁?

fx(f1)
fx(f2)
