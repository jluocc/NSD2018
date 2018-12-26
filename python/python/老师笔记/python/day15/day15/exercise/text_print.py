# 练习:
#   写一个程序,读入任意行的文字,当输入空行时结束输入
#   打印带有行号的输入结果
#   如:
#      请输入: tarena<回车>
#      请输入: china<回车>
#      请输入: holiday<回车>
#      请输入: <回车>
#     输出如下:
#      第1行: tarena
#      第2行: china
#      第3行: holiday


def get_input_text():
    "输入一些文字,形成列表后返回"
    L = []
    while True:
        s = input("请输入: ")
        if not s:
            return L
        L.append(s)

def print_text_with_number(L):
    # 用enumerate将L形成能提供行号的可迭代对象
    for t in enumerate(L, 1):
        print("第%d行: %s" % t)

L = get_input_text()
print_text_with_number(L)
