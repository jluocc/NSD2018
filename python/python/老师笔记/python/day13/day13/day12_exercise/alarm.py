# 3. 编写一个闹种程序,启动时设置定时时间,到时间后打印一句"时间到!",然后退出程序

import time

def alarm(h, m):  # h小时,m分钟
    print("设置时间为: %02d:%02d" % (h,m))
    while True:
        # 得到当前时间的小时和分钟:
        # t = time.localtime()[3:5]
        t = time.localtime()
        t2 = t[3:5]
        if t2 == (h, m):  # 判断时间
            print("时间到!!!")
            break
        # 显示时间
        print("%02d:%02d:%02d" % t[3:6],
              end='\r')
        # 睡一秒
        time.sleep(1)


hour = int(input("请输入小时: "))
minute = int(input("请输入分钟: "))
alarm(hour, minute)
