# binary_file_write.py

# 0x00 0x01 0x02  ... 0xFF  # 256个

try:
    f = open("0_255.bin", 'wb') # 二进制写
    b = bytes(range(256))
    f.write(b)

    f.close()
    print("写数据成功")
except OSError:
    print("写文件失败!")