from .BasicModel import Base, BasePoint
from ..Canvas import Canvas


class Line(Base):

    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.p1 = BasePoint(x1, y1, z1)
        self.p2 = BasePoint(x2, y2, z2)

    def draw(self):
        # 竖线和点
        if self.p1.x == self.p2.x:
            if self.p1.z < self.p2.z:
                for i in range(int(self.p1.z), int(self.p2.z) + 1):
                    Canvas.draw(self.p1.x, i)
            else:
                for i in range(int(self.p2.z), int(self.p1.z) + 1):
                    Canvas.draw(self.p1.x, i)
                return self
        k = (self.p2.z - self.p1.z) / (self.p2.x - self.p1.x)
        # 斜率绝对值小于1，在x轴采样点更多
        if abs(k) < 1:
            if self.p1.x < self.p2.x:
                for i in range(int(self.p1.x), int(self.p2.x) + 1):
                    Canvas.draw(i, int(self.p1.z + k * (i - self.p1.x)))
            else:
                for i in range(int(self.p2.x), int(self.p1.x) + 1):
                    Canvas.draw(i, int(self.p1.z + k * (i - self.p1.x)))

        # 斜率绝对值大于1，在y轴采样点更多
        else:
            if self.p1.z < self.p2.z:
                for i in range(int(self.p1.z), int(self.p2.z) + 1):
                    Canvas.draw(int(self.p1.x + (i - self.p1.z) / k), i)
            else:
                for i in range(int(self.p2.z), int(self.p1.z) + 1):
                    Canvas.draw(int(self.p1.x + (i - self.p1.z) / k), i)

        return self

    def translate(self, dx, dy, dz):
        self.p1.translate(dx, dy, dz)
        self.p2.translate(dx, dy, dz)
        return self

    def scale(self, sx, sy, sz):
        # tx, ty, tz = self.p1.x, self.p1.y, self.p1.z
        # self.translate(-tx, -ty, -tz)
        self.p1.scale(sx, sy, sz)
        self.p2.scale(sx, sy, sz)
        # self.translate(tx, ty, tz)
        return self

    def rotatex(self, theta):
        self.p1.rotatex(theta)
        self.p2.rotatex(theta)
        return self

    def rotatey(self, theta):
        self.p1.rotatey(theta)
        self.p2.rotatey(theta)
        return self

    def rotatez(self, theta):
        self.p1.rotatez(theta)
        self.p2.rotatez(theta)
        return self
