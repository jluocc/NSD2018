# 2. 写程序求:
#  1/1 + 1/3 + 1/5 + 1/7 + ..... + 1/99的和

fenmu = 1
he = 0.0
while fenmu < 100:
    he += 1 / fenmu
    fenmu += 2

print("和是:", he)