

def goodbye(L):
    for x in L:
        print("再见:", x)

def hello(L):
    for x in L:
        print("您好:", x)

def fx(fn, L):
    fn(L)

fx(hello, ["Tom", "Jerry", "Spike"])
