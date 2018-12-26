# recursion.py


# 此示例示意递归调用和根据条件结束递归
def fx(n):
    print("递归进入第", n, "层")
    if n == 3:
        return
    fx(n + 1)  # 进入下一层
    print("递归退出第", n, "层")

fx(1)
print('程序结束')