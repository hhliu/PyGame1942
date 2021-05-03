"""
使用pygame撰寫一個簡單的射擊遊戲
不使用pygame.sprite.Sprite，練習物件導向以及事件導向的撰寫
"""
import pygame
from pathlib import Path

# 初始化pygame系統
from PyGame1945.code.player import Player

pygame.init()
# 建立視窗物件，寬、高
screenHigh = 760
screenWidth = 1000
playground = [screenWidth, screenHigh]
screen = pygame.display.set_mode((screenWidth, screenHigh))

parent_path = Path(__file__).parents[1]
image_path = parent_path / 'res'
icon_path = image_path / 'airplaneicon.png'
# Title, Icon, and Background
pygame.display.set_caption("1942偽")
icon = pygame.image.load(icon_path)  # 載入圖示
pygame.display.set_icon(icon)
background = pygame.Surface(screen.get_size())
background = background.convert()  # 改變pixel format，加快顯示速度
background.fill((50, 50, 50))  # 畫布為鐵黑色(三個參數為RGB)

fps = 120  # 更新頻率，包含畫面更新與事件更新
movingScale = 600 / fps  # 大約 600 pixels / sec
# Player，playground為必要參數
player = Player(playground=playground, sensitivity=movingScale)

running = True
clock = pygame.time.Clock()  # create an object to help track time
# 設定無窮迴圈，讓視窗持續更新與執行
while running:
    # 從pygame事件佇列中，一項一項的檢查
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))  # 更新背景圖片

    # 添加player圖片
    player.update()
    screen.blit(player.image, player.xy)
    pygame.display.update()  # 更新螢幕狀態
    dt = clock.tick(fps)  # 每秒更新fps次，This method should be called once per frame.
pygame.quit()  # 關閉繪圖視窗
