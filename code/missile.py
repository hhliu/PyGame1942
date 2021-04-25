from pathlib import Path
from typing import Union
import pygame
from pygame.surface import Surface, SurfaceType


# 飛彈類別
class Missile:
    changeX = 0
    changeY = 0

    # 建構式
    def __init__(self, x=350, y=500, playground=None, sensitivity=1):
        if playground is None:
            playground = [1200, 900]
        self.x = x  # 座標屬性
        self.y = y  #
        self.available = True

        # 左右邊界不重要，上邊界等整個飛彈離開螢幕時觸發
        self.missileBound = (0, playground[0], -50, playground[1] - 100)  # 右, 左, 上, 下
        self.moveScale = 1 + 0.7 * sensitivity

        parent_path = Path(__file__).parents[1]
        self.missile_path = parent_path / 'res' / 'missile2.png'
        self.missileImage = pygame.image.load(self.missile_path)

    # 解構子，目前沒用
    def __del__(self):
        print("I'm being automatically destroyed. Goodbye!")

    # 傳統getter撰寫方式
    def get_image(self) -> Union[Surface, SurfaceType]:
        return self.missileImage

    # Python提供的getter，可以使用與變數同名
    @property
    def xy(self):
        return [self.x, self.y]

    # Python提供的setter，可以與變數同名
    @xy.setter
    def xy(self, xy):
        try:
            self.x, self.y = xy
            if self.x > self.missileBound[1]:
                self.x = self.missileBound[1]
            if self.x < self.missileBound[0]:
                self.x = self.missileBound[0]
            if self.y > self.missileBound[3]:
                self.y = self.missileBound[3]
            if self.y < self.missileBound[2]:
                self.y = self.missileBound[2]
        except ValueError:
            raise ValueError("Pass an iterable with two items")
        else:
            """ This will run only if no exception was raised """
            pass

    def to_the_top(self):
        self.changeY = -self.moveScale

    # 只會往上
    def move_xy(self):
        self.y += self.changeY
        if self.y > self.missileBound[3]:
            # 超過螢幕範圍，標記為失效
            self.available = False
        return [self.x, self.y]
