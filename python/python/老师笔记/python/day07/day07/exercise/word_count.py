# 练习:
#   输入一段字符串,打印出这个字符串中出现过的字符及出现过的次数
#   如:
#     输入:ABCDABCABA
#   打印:
#     a: 4次
#     b: 3次
#     d: 1次
#     c: 2次

s = input("请输入文字: ")  # ABCDABCABA
# 方法1 用字典来存储数据,键为字母,值为出现次数
# d = {}
# for ch in s:  # ch绑定每一个字符
#     # 1. 判断如果ch已经出现过,将原有计数加1
#     if ch in d:
#         d[ch] = d[ch] + 1  # d[ch] += 1 
#     # 2. ch没有出现过,要在d内创建ch键,值为1
#     else:
#         d[ch] = 1

# # 打印结果
# for k, v in d.items():
#     print(k,':', v, '次')

# 方法2
# 先将字符串去重,放入到列表L中
L = []  # 用来存放出现过的字符
for ch in s:
    # 如果ch没有在L中,说明第一次出现,放到的L中
    if ch not in L:
        L.append(ch)
# print(L)
for ch in L:
    print(ch, ":", s.count(ch), '次')
