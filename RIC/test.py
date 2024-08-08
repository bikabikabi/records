import time

from RIC.Model import *
from RIC.Canvas import *

canvas = Canvas(550, 100)
c = Cuboid(30, 30, 30, -30, -30, -30)
canvas.register_graphic(c)
# 把角度转换为弧度
theta_x, theta_y, theta_z = -1, 3, -1  # 初始化旋转角度
last_time = time.time()
while True:
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time
    # 应用变换
    c.rotatex(theta_x).rotatey(theta_y).rotatez(theta_z)

    canvas.update()
    canvas.flush()
    # time.sleep(0.008)
    time_to_wait = 1 / 60 - delta_time
    if time_to_wait > 0:
        time.sleep(time_to_wait)
