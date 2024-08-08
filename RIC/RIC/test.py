import time

from RIC.Model import *
from RIC.Canvas import *

# 创建一个画布实例，尺寸为550x100
canvas = Canvas(550, 100)

# 创建一个长方体对象，长宽高均为60，原点位于长方体中心
c = Cuboid(30, 30, 30, -30, -30, -30)
# 将长方体对象注册到画布上
canvas.register_graphic(c)
# 初始化各轴的旋转角度
theta_x, theta_y, theta_z = -1, 3, -1
# 记录上次的时间戳
last_time = time.time()
while True:
    # 获取当前时间戳
    current_time = time.time()
    # 计算时间差
    delta_time = current_time - last_time
    # 更新上次的时间戳
    last_time = current_time
    # 应用变换，围绕x、y、z轴旋转
    c.rotatex(theta_x).rotatey(theta_y).rotatez(theta_z)
    # 更新画布，将图形绘制到画布上
    canvas.update()
    # 将画布的内容输出到控制台并清空
    canvas.flush()

    # 计算还需要等待的时间，以达到约30帧每秒的刷新率
    time_to_wait = 1 / 30 - delta_time
    # 如果还需要等待的时间大于0，则进行等待
    if time_to_wait > 0:
        time.sleep(time_to_wait)
