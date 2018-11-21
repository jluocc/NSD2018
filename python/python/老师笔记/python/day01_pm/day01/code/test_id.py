
# 经过优化后，两个10000可能会合并成为一个10000
a = 10000
b = 10000
print(id(a))
print(id(b))
print(a is b)  # True or False?
