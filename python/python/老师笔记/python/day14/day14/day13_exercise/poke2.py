# 练习:
#   1. 模拟斗地主发牌,扑克牌54张
#     花色:
#       黑桃('\u2660'), 梅花('\u2663'), 红桃('\u2665'), 方块('\u2666')
#     数字:
#       A2-10JQK
#       大王,小王
#     三个人,每个人发17张牌,底牌留三张
#       输入回车,打印第1个人的17张牌
#       输入回车,打印第2个人的17张牌
#       输入回车,打印第3个人的17张牌
#       输入回车,打印3张底牌


poke = ["大王", "小王"]
kinds = ['\u2660', '\u2663', '\u2665','\u2666']
numbers = ['A'] + [str(x) for x in range(2, 11)] + list("JQK")

for k in kinds:
    for n in numbers:
        poke.append(k + n)

poke2 = poke.copy()
# 洗牌
import random
random.shuffle(poke2)

play1 = poke2[:17]  # 发给玩家1
# 从poke中删除玩家1拿到的17张牌
# 此方法是对的
# for x in play1:
#     if x in poke2:
#         poke2.remove(x)
# print("剩余的牌是%d张" % len(poke2))

# 以下做法是错的
for x in poke2:
    if x in play1:
        poke2.remove(x)
print("剩余的牌是%d张" % len(poke2))

# 以处略过.....