"""
使用pygame撰寫一個簡單的射擊遊戲
不使用pygame.sprite.Sprite，練習物件導向以及事件導向的撰寫
"""
import pygame
# 初始化pygame系統
pygame.init()
# 建立視窗物件，寬、高
screenHigh = 760
screenWidth = 1000
playground = [screenWidth, screenHigh]
screen = pygame.display.set_mode((screenWidth, screenHigh))

running = True
fps = 120   # 更新頻率，包含畫面更新與事件更新
clock = pygame.time.Clock()   # create an object to help track time
# 設定無窮迴圈，讓視窗持續更新與執行
while running:
    # 從pygame事件佇列中，一項一項的檢查
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update() # 更新螢幕狀態
    dt = clock.tick(fps) # 每秒更新fps次
pygame.quit()  # 關閉繪圖視窗
