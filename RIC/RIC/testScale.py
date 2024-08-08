import time

from RIC.Model import *
from RIC.Canvas import *

# 创建一个画布实例，尺寸为550x100
canvas = Canvas(550, 500)

# 创建一个长方体对象，长宽高均为60，原点位于长方体中心
c = Cuboid(30, 30, 30, -30, -30, -30)
# 将长方体对象注册到画布上
canvas.register_graphic(c)
c.rotatex(10).rotatez(10)
c.scale(3, 1, 1)
canvas.clear_console()
canvas.update()
canvas.flush()
