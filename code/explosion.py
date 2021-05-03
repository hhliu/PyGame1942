from pathlib import Path
import random
import pygame
import math
from object import GameObject


# 爆炸類別
class Explosion(GameObject):
    # 全域、靜態變數
    explosion_effect = []

    # 建構式
    def __init__(self, xy=None):
        GameObject.__init__(self)
        if xy is None:
            self._available = False
        else:
            self._center = xy  # 座標屬性

        if Explosion.explosion_effect:
            pass
        else:
            __parent_path = Path(__file__).parents[1]
            icon_path = __parent_path / 'res' / 'explosion_small.png'
            Explosion.explosion_effect.append(pygame.image.load(icon_path))
            icon_path = __parent_path / 'res' / 'explosion_medium.png'
            Explosion.explosion_effect.append(pygame.image.load(icon_path))
            icon_path = __parent_path / 'res' / 'explosion_large.png'
            Explosion.explosion_effect.append(pygame.image.load(icon_path))
            Explosion.explosion_effect.append(pygame.image.load(icon_path))
            icon_path = __parent_path / 'res' / 'explosion_medium.png'
            Explosion.explosion_effect.append(pygame.image.load(icon_path))

        self.__image_index = 0
        self._image = Explosion.explosion_effect[self.__image_index]
        self._x = self._center[0] - (self._image.get_rect().w / 2)
        self._y = self._center[1] - (self._image.get_rect().h / 2)
        self.__fps_count = 0

    # 解構子，目前沒用
    def __del__(self):
        print("Explosion is being automatically destroyed.")

    def update(self):
        self.__fps_count += 1
        if self.__fps_count > 30:
            self.__image_index += 1
            if self.__image_index > 4:
                self._available = False
            else:
                self._image = Explosion.explosion_effect[self.__image_index]
                self._x = self._center[0] - (self._image.get_rect().w / 2)
                self._y = self._center[1] - (self._image.get_rect().h / 2)
