import pygame
from pathlib import Path
from code.player import Player

parent_path = Path(__file__).parents[1]
image_path = parent_path / 'res'
icon_path = image_path / 'airplaneicon.png'
player_path = image_path / 'airforce.png'

# 初始化pygame系統
pygame.init()
# 建立視窗物件，寬1200、高900
screenHigh = 900
screenWidth = 1200
playground = [screenWidth, screenHigh]
fps = 120
keySensitivity = 600 / fps
screen = pygame.display.set_mode((screenWidth, screenHigh))

# Title, Icon, and Background
pygame.display.set_caption("1942偽")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)
background = pygame.Surface(screen.get_size())
background = background.convert() # 為畫布建立副本，加快顯示速度
background.fill((50,50,50))  # 畫布為白色(三個參數為RGB)

# Player
player = Player(540, 600, playground, keySensitivity)

# 設定無窮迴圈，讓視窗持續更新與執行
running = True

keyCountX = 0  # 可以不用寫這行，這是基於C語言的習慣
keyCountY = 0

clock = pygame.time.Clock()
dt = 0

# 建立事件編號
launchMissile = pygame.USEREVENT + 1

while running:

    # 從pygame事件佇列中，一項一項的檢查
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keyCountX += 1
                player.to_the_right()
            if event.key == pygame.K_d:
                keyCountX += 1
                player.to_the_left()
            if event.key == pygame.K_s:
                keyCountY += 1
                player.to_the_bottom()
            if event.key == pygame.K_w:
                keyCountY += 1
                player.to_the_top()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                if keyCountX == 1:
                    keyCountX = 0
                    player.stop_x()
                else:
                    keyCountX -= 1
            if event.key == pygame.K_s or event.key == pygame.K_w:
                if keyCountY == 1:
                    keyCountY = 0
                    player.stop_y()
                else:
                    keyCountY -= 1

    screen.blit(background, (0, 0))
    # 添加player圖片
    screen.blit(player.playerImage, player.move_xy())
    # 更新螢幕狀態
    pygame.display.update()
    dt = clock.tick(fps)

pygame.quit()  # 關閉繪圖視窗
