# 练习:
# names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 排序的依据是'moT'  'yrreJ', 'ekipS' 'ekyT'
# 结果是:
#     ['Spike', 'Tyke', 'Tom', 'Jerry']
#     (注:如果没有现成的函数可用,需要自己写函数)



names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 排序的依据是'moT'  'yrreJ', 'ekipS' 'ekyT'

def fk(s):
    r =  s[::-1]
    print("字符串", s, '排序的依据是', r)
    return r

L = sorted(names, key=fk)
print(L)
# 结果是:
#     ['Spike', 'Tyke', 'Tom', 'Jerry']
#     (注:如果没有现成的函数可用,需要自己写函数)

