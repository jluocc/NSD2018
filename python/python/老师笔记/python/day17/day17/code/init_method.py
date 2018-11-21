# init_method.py


# 此示例示意初始化方法的定义及自动调用
class Car:
    def __init__(self, c, b, m):
        self.color = c  # 颜色
        self.brand = b  # 品牌
        self.model = m  # 型号
        print("初始化方法被调用")

    def run(self, speed):
        print(self.color, '的',
              self.brand, self.model,
              "正在以", speed,
              '公里/小时的速度行驶')


a4 = Car("红色", '奥迪', 'A4')
a4.run(199)

t1 = Car("蓝色", "TESLA", "Model S")
t1.run(230)
