

import time

f = open("myflush.txt", 'w')
f.write("aaaaaaaaaaaaaaaaaaaaaaaaaa")
f.flush()  # 强制清空缓冲区

while True:
    time.sleep(0.1)

f.close()
