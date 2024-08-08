import math
import os
from abc import ABC, abstractmethod
from ..Canvas import Canvas


class Base(ABC):

    @abstractmethod
    def translate(self, dx, dy, dz):
        ...

    @abstractmethod
    def scale(self, sx, sy, sz):
        ...

    @abstractmethod
    def rotatex(self, theta):
        ...

    @abstractmethod
    def rotatey(self, theta):
        ...

    @abstractmethod
    def rotatez(self, theta):
        ...

    @abstractmethod
    def draw(self):
        ...


class BasePoint(Base):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        self.__canvas.draw(self.x, self.z)

    def translate(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz
        return self

    def scale(self, sx, sy, sz):
        self.x *= sx
        self.y *= sy
        self.z *= sz
        return self

    def rotatex(self, theta):
        # 转换为弧度
        theta = math.radians(theta)
        t_y = self.y * math.cos(theta) - self.z * math.sin(theta)
        t_z = self.y * math.sin(theta) + self.z * math.cos(theta)
        self.y = t_y
        self.z = t_z
        return self

    def rotatey(self, theta):
        theta = math.radians(theta)
        t_x = self.x * math.cos(theta) + self.z * math.sin(theta)
        t_z = -self.x * math.sin(theta) + self.z * math.cos(theta)
        self.x = t_x
        self.z = t_z
        return self

    def rotatez(self, theta):
        theta = math.radians(theta)
        t_x = self.x * math.cos(theta) - self.y * math.sin(theta)
        t_y = self.x * math.sin(theta) + self.y * math.cos(theta)
        self.x = t_x
        self.y = t_y
        return self
