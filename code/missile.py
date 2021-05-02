from pathlib import Path
import pygame
from object import GameObject
import math


# 飛彈類別
class Missile(GameObject):

    # 建構式
    def __init__(self, xy=(540, 600), playground=None, sensitivity=1):
        GameObject.__init__(self, playground)
        self._x = xy[0]  # 座標屬性
        self._y = xy[1]  #

        # 左右邊界不重要，上邊界等整個飛彈離開螢幕時觸發
        self._objectBound = (0, playground[0], -50, playground[1] - 100)  # 右, 左, 上, 下
        self._moveScale = 0.7 * sensitivity

        __parent_path = Path(__file__).parents[1]
        self.__missile_path = __parent_path / 'res' / 'missile2.png'
        self._image = pygame.image.load(self.__missile_path)
        self._center = self._x + self._image.get_rect().w / 2, self._y + self._image.get_rect().w / 2
        self._radius = self._image.get_rect().w / 2

        self.to_the_top()

    # 解構子，目前沒用
    def __del__(self):
        print("I'm being automatically destroyed. Goodbye!")

    # 只會往上，override parent's method
    def update(self):
        self._y += self._changeY
        if self._y < self._objectBound[2]:
            # 超過螢幕範圍，標記為失效
            self._available = False

        self._center = self._x + self._image.get_rect().w / 2, self._y + self._image.get_rect().w / 2

    def collision_detect(self, enemies):
        for m in enemies:
            if self._collided_(m):
                self._hp -= 10
                self._collided = True
                self._available = False
                m.hp = -1
                m.collided = True
                m.available = False
