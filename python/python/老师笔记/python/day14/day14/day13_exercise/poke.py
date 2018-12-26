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
play2 = poke2[17:34]  # 发给玩家2
play3 = poke2[34:51]  # 发给玩家3
dipai = poke2[51:]  # 底牌
poke2.clear()  # del poke2

# 三个人,每个人发17张牌,底牌留三张
#   输入回车,打印第1个人的17张牌
input("请输入回车键发给第一个人:")
print(play1)
input("请输入回车键发给第二个人:")
print(play2)
input("请输入回车键发给第三个人:")
print(play3)
input("请输入回车键发底牌:")
print(dipai)
