# temperature.py


# 4. 温度转换
# 摄氏湿度 = 5.0 / 9.0*(华氏温度-32)
# 开氏温度 = 摄氏温度 + 273.15
# 请问:
#     100华氏温度转为摄氏温度是多少度?
#     转为开氏温度是多少度?

huashi = 100
sheshi = 5.0 / 9.0 * (huashi - 32)
kaishi = sheshi + 273.15
print("100华氏温度为", sheshi, '摄氏度')
print("100华氏温度为", kaishi, '开氏度')