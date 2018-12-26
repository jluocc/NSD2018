#   1. 写一个函数get_chinese_char_count(s) 函数,此函数实现的功能是给定一个字符串,返回这个字符串中中文字符的个数
#     def get_chinese_char_count(s):
#         .... # 此处自己实现
    
#     s = input("请输入中英文混合的字符串: ")
#     print("您输入的中文字符的个数是:", 
#            get_chinese_char_count(s))

def get_chinese_char_count(s):
    count = 0  # 记录中文字符的个数
    # 此处用来记中文数
    for ch in s:
        if ord(ch) > 127:
            count += 1

    return count


s = input("请输入中英文混合的字符串: ")
print("您输入的中文字符的个数是:", 
        get_chinese_char_count(s))