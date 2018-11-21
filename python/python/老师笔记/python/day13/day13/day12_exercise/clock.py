#   2. 写一个程序,以电子时钟格式显示时间:
#      格式为:
#        HH:MM:SS   如: 15:58:26

import time

def clock_run():
    while True:
        # 拿到当前时间元组
        t = time.localtime()
        # 显示时间
        print("%02d:%02d:%02d"
                # % (t[3],t[4], t[5]),
                % t[3:6],
                end='\r')
        # 睡眠一秒再运行.可以节约CPU的占用时间
        time.sleep(1)
        



clock_run()