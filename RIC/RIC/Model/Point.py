from .BasicModel import BasePoint
from ..Canvas import Canvas


class Point(BasePoint):
 
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
