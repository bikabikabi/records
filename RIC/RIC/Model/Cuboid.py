from .BasicModel import Base
from ..Canvas import Canvas
from .Line import Line


class Cuboid(Base):

    def __init__(self, x1, y1, z1, x2, y2, z2):

        self.lines = [
            Line(x1, y1, z1, x2, y1, z1),
            Line(x1, y1, z1, x1, y2, z1),
            Line(x1, y1, z1, x1, y1, z2),

            Line(x2, y1, z1, x2, y2, z1),
            Line(x2, y1, z1, x2, y1, z2),

            Line(x1, y2, z1, x2, y2, z1),
            Line(x1, y2, z1, x1, y2, z2),

            Line(x1, y1, z2, x2, y1, z2),
            Line(x1, y1, z2, x1, y2, z2),

            Line(x2, y2, z1, x2, y2, z2),
            Line(x2, y1, z2, x2, y2, z2),
            Line(x1, y2, z2, x2, y2, z2),

        ]

    def draw(self):
        for line in self.lines:
            line.draw()

    def translate(self, dx, dy, dz):
        for line in self.lines:
            line.translate(dx, dy, dz)
        return self

    def scale(self, sx, sy, sz):
        center_x = (self.lines[0].p1.x + self.lines[-1].p2.x) / 2
        center_y = (self.lines[0].p1.y + self.lines[-1].p1.y) / 2
        center_z = (self.lines[0].p1.z + self.lines[-1].p1.z) / 2
        for line in self.lines:
            line.translate(-center_x, -center_y, -center_z)
            line.scale(sx, sy, sz)
            line.translate(center_x, center_y, center_z)

        return self

    def rotatex(self, theta):
        for line in self.lines:
            line.rotatex(theta)
        return self

    def rotatey(self, theta):
        for line in self.lines:
            line.rotatey(theta)
        return self

    def rotatez(self, theta):
        for line in self.lines:
            line.rotatez(theta)
        return self
