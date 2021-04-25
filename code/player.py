from pathlib import Path
from typing import Union
import pygame
from pygame.surface import Surface, SurfaceType


# 玩家類別
class Player:
    changeX = 0
    changeY = 0

    # 建構式
    def __init__(self, x=350, y=500, playground=None, sensitivity=1):
        if playground is None:
            playground = [1200, 900]
        self.x = x  # 顏色屬性
        self.y = y  # 座位屬性
        self.playerBound = (10, playground[0] - 130, 10, playground[1] - 100)  # 右, 左, 上, 下
        self.moveScale = 1 + 0.5 * sensitivity

        parent_path = Path(__file__).parents[1]
        self.player_path = parent_path / 'res' / 'airforce.png'
        self.playerImage = pygame.image.load(self.player_path)

    # 傳統getter撰寫方式
    def get_image(self) -> Union[Surface, SurfaceType]:
        return self.playerImage

    # Python提供的getter，可以使用與變數同名
    @property
    def xy(self):
        return [self.x, self.y]

    # Python提供的setter，可以與變數同名
    @xy.setter
    def xy(self, xy):
        try:
            self.x, self.y = xy
            if self.x > self.playerBound[1]:
                self.x = self.playerBound[1]
            if self.x < self.playerBound[0]:
                self.x = self.playerBound[0]
            if self.y > self.playerBound[3]:
                self.y = self.playerBound[3]
            if self.y < self.playerBound[2]:
                self.y = self.playerBound[2]
        except ValueError:
            raise ValueError("Pass an iterable with two items")
        else:
            """ This will run only if no exception was raised """
            pass

    def to_the_left(self):
        self.changeX = self.moveScale

    def to_the_right(self):
        self.changeX = -self.moveScale

    def to_the_bottom(self):
        self.changeY = self.moveScale

    def to_the_top(self):
        self.changeY = -self.moveScale

    def stop_x(self):
        self.changeX = 0

    def stop_y(self):
        self.changeY = 0

    def move_xy(self):
        self.x += self.changeX
        self.y += self.changeY

        if self.x > self.playerBound[1]:
            self.x = self.playerBound[1]
        if self.x < self.playerBound[0]:
            self.x = self.playerBound[0]
        if self.y > self.playerBound[3]:
            self.y = self.playerBound[3]
        if self.y < self.playerBound[2]:
            self.y = self.playerBound[2]

        return [self.x, self.y]
