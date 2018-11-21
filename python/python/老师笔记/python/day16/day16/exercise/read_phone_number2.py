# read_phone_number.py

# 1. 打开文件
# myfile = open("pbase/day16/exercise/data.txt")
myfile = open("./data.txt")

# 2. 读取文件数据,并打印为相应格式
# 方法2, 先读取所有文字到内存中,形成列表
lines = myfile.readlines()
for line in lines:
    line = line.strip()  # 去掉末尾的'\n'
    L = line.split()  # 将其拆分为字符串列表
            # L=['小李', '13888888888']
    print('姓名:', L[0], "电话:", L[1])



# 3. 关闭文件
myfile.close()