# 练习:
#   经理有: 曹操,刘备,孙权
#   技术员有: 曹操,孙权,张飞,关羽
#   用集合求:
#     1. 即是经理也是技术员的人有谁?
#     2. 是经理,但不是技术员的人有谁?
#     3. 是技术员,但不是经理的人有谁?
#     4. 张飞是经理吗?
#     5. 身兼一职的人有谁?
#     6. 经理和技术员共有几个人?


manager = {'曹操', '刘备', '孙权'}
techs = {'曹操', '孙权', '张飞', '关羽'}

print("即是经理也是技术员的人有:", manager & techs)
print("是经理,但不是技术员的人有:",
       manager - techs)
print("是技术员,但不是经理的人有:",
       techs - manager)

if '张飞' in manager:
    print("张飞是经理!")
else:
    print("张飞不是经理!")

print("身兼一职的人有:", manager ^ techs)
print("经理和技术员共有%d个人" %
       len(manager | techs))
