#   4. BMI(Body Mass Index) 指数,又称身体质量指数
#     BMI公式:  BMI = 体重(公斤) / 身高的平方(米)
#     标准表:
#       BMI < 18.5       体重过轻
#       18.5 <= BMI < 24 正常范围 
#       BMI >= 24         体重过重(超标)
#     输入身高和体重,打印BMI值,并打印体重状况

height = float(input("请输入身高(米): "))
weight = float(input("请输入体重(kg): "))

bmi = weight / height ** 2
print("BMI:", bmi)

if bmi < 18.5:
    print("体重过轻")
elif 18.5 <= bmi < 24:
    print("正常范围")
else:
    print("体重过重")


