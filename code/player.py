from pathlib import Path
from typing import Union
import pygame
from pygame.surface import Surface, SurfaceType
from object import GameObject
import math

# 玩家類別
class Player(GameObject):

    # 建構式
    def __init__(self, xy=(540, 600), playground=None, sensitivity=1):
        GameObject.__init__(self, playground)
        self._x = xy[0]  # 位置屬性
        self._y = xy[1]  #
        self._objectBound = (10, playground[0] - 130, 10, playground[1] - 100)  # 左, 右, 上, 下
        self._moveScale = 0.5 * sensitivity

        __parent_path = Path(__file__).parents[1]
        self.__player_path = __parent_path / 'res' / 'airforce.png'
        self._image = pygame.image.load(self.__player_path)
        self._center = self._x + self._image.get_rect().w / 2, self._y + self._image.get_rect().h / 2
        self._radius = 0.3 * math.hypot(self._image.get_rect().w, self._image.get_rect().h)
        # print(self._image.get_rect().w, self._image.get_rect().h, self._center, self._radius)

    # 傳統getter撰寫方式
    def get_image(self) -> Union[Surface, SurfaceType]:
        return self._image

    def update(self):
        GameObject.update(self)
        self._center = self._x + self._image.get_rect().w / 2, self._y + self._image.get_rect().h / 2

    def collision_detect(self, enemies):
        for m in enemies:
            if self._collided_(m):
                self._hp -= 10
                self._collided = True
                m.hp = -1
                m.collided = True
                m.available = False








