#   创建一个字典:
#     d = {'name': 'tarena', 'age':15}
#     为此字典添加地址(address)键,对应的值为"北京市海淀区",如果如下:
#     d = {'name': 'tarena', 'age':15, 'address': "北京市海淀区"}

# 创建字典
d = {'name': 'tarena', 'age':15} # 字面值
d = dict(name='tarena', age=15)#关键字传参
d = dict(
    (['name', 'tarena'], ('age', 15))
    )  # 用可迭代对象创建字典
d = {}
d['name'] = 'tarena'
d['age'] = 15

print('d=', d)
d['address'] = '北京市海淀区'
print('d=', d)

