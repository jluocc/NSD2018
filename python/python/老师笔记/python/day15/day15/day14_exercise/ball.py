#   1. 一个球从100米高空落下,每次落地后反弹高度为原高度的一半地,再落下,
#     1) 写程序算出皮球在第10次落地后反弹多高
#     2) 打印10次后球出共经过多少米路程

def get_last_height(meter, times):
    '''根据小于的初始高度meter和次数,返回最后的反弹高度'''
    for _ in range(times):
        meter /= 2
    return meter

print("球第10次落地后的高度是:",
      get_last_height(100, 10))
    
def get_distance(meter, times):
    s = 0  # 记录球的总行程
    for _ in range(times):
        # 记录下落时行程
        s += meter
        # 算出反弹高度
        meter /= 2
        # 记录反弹的行程
        s += meter

    return s

print("球在第10次反弹后的总行程是:", 
      get_distance(100, 10), "米")






