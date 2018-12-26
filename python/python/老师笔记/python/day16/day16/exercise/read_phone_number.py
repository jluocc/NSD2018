# read_phone_number.py

# 1. 打开文件
myfile = open("pbase/day16/exercise/data.txt")
# myfile = open("./data.txt")

# 2. 读取文件数据,并打印为相应格式
# 方法1,每次读取一行,然后进行处理后打印
while True:
    line = myfile.readline()
    if line == '':
        break
    line = line.strip()  # 去掉末尾的'\n'
    L = line.split()  # 将其拆分为字符串列表
            # L=['小李', '13888888888']
    print('姓名:', L[0], "电话:", L[1])

# 3. 关闭文件
myfile.close()