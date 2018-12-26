# while_embed_break.py

# 此示例示意循环嵌套
j = 1
while j <= 10:
    i = 1
    while i <= 20:
        print(i, end=' ')
        if i == 10:
            break
        i += 1
    print()
    j += 1

print("程序结束")
