#   查看
#     >>> help(print)
#   猜想print()函数是形参列表是如何定义的?

def myprint(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)

myprint()
myprint(1,2,3,4)
myprint(1,2,3,4,sep="#")
myprint(1,2,3,4,sep="#", end="\n\n")
myprint('==========================')