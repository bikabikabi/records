import os
import sys
from copy import deepcopy


class Canvas:
    __instance = None
    __is_init = False
    __graphics = []
    __clean = None
    __cache = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, width=100, height=100):

        self.width = width
        self.height = height
        # 空白绘板
        Canvas.__clean = [[' ' for _ in range(width)] for _ in range(height)]

        # 缓存绘板
        Canvas.__cache = deepcopy(self.__clean)
        # 注册图形

    @classmethod
    def draw(cls, x, z):
        # 判断是否在可视范围
        if x <= -cls.__instance.width / 2 or x >= cls.__instance.width / 2:
            return
        if z <= -cls.__instance.height / 2 or z >= cls.__instance.height / 2:
            return
        # 将世界坐标变换为屏幕坐标，以中心为原点。
        x = int(x + cls.__instance.width / 2)
        z = int(z + cls.__instance.height / 2)
        Canvas.__cache[z][x] = '■'

    @classmethod
    def update(cls):
        for graphic in cls.__graphics:
            graphic.draw()

    @classmethod
    def clear_console(cls):
        os.system('cls')

    @classmethod
    def flush(cls):
        cls.clear_console()

        sys.stdout.write('\n'.join(''.join(line) for line in reversed(cls.__cache)))
        sys.stdout.flush()
        cls.__cache = deepcopy(cls.__clean)

    @classmethod
    def register_graphic(cls, graphic):

        cls.__graphics.append(graphic)
