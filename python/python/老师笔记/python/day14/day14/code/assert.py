# assert.py


# 此示例示意assert 语句的用法:
def get_score():
    s = int(input("请输入学生成绩:(0~100): "))
    assert 0 <= s <= 100, "成绩超出范围"
    # if bool(0 <= s <= 100) == False:
    #     raise AssertionError("成绩超出范围")
    return s

try:
    score = get_score()
    print("学生的成绩为:", score)
except AssertionError as err:
    print("AssertionError类型的错误被触发,且已捕获")
    print("err=", err)

