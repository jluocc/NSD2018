# read_phone_number.py

# 1. 打开文件
# myfile = open("pbase/day16/exercise/data.txt")
myfile = open("./data.txt")

# 2. 读取文件数据,并打印为相应格式
# 方法3, 用read读取数据到内存中,然后再分行处理
s = myfile.read()

lines = s.split('\n')  # 以换行符进行拆分
for line in lines:
    L = line.split()  # 将其拆分为字符串列表
            # L=['小李', '13888888888']
    print('姓名:', L[0], "电话:", L[1])

# 3. 关闭文件
myfile.close()