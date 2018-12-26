# try-finally.py

# 此示例示意,try-finally语句用法
# 以煎蛋, 打开天燃气, 关闭天燃气
def fry_egg():
    print("打开天燃气...")
    try:
        count = int(input("请输入鸡蛋个数:"))
        print("完成煎蛋,共煎了%d个鸡蛋" % count)
    finally:
        print("关闭天燃气")

try:
    fry_egg()
except:
    print("煎鸡蛋时发生异常, 已转为正常状态")
    



        