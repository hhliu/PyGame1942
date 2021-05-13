"""
使用pygame撰寫一個簡單的射擊遊戲
不使用pygame.sprite.Sprite，練習物件導向以及事件導向的撰寫
"""
import pygame
from pathlib import Path
from explosion import Explosion
from enemy import Enemy
from missile import MyMissile
from player import Player

# 初始化pygame系統
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
background.fill((50, 50, 50))  # 畫布為鐵黑色(三個參數為RGB)
background = background.convert()  # 改變pixel format，加快顯示速度

fps = 120  # 更新頻率，包含畫面更新與事件更新
movingScale = 600 / fps  # 大約 600 pixels / sec
# Player，playground為必要參數
player = Player(playground=playground, sensitivity=movingScale)

# 建立物件串列
Missiles = []
Enemies = []
Boom = []

keyCountX = 0   # 用來計算按鍵備按下的次數，x軸一組
keyCountY = 0

# 建立事件編號
launchMissile = pygame.USEREVENT + 1
createEnemy = pygame.USEREVENT + 2
explosion = pygame.USEREVENT + 3

# 建立敵機，每秒一台
pygame.time.set_timer(createEnemy, 1000)

running = True
clock = pygame.time.Clock()  # create an object to help track time

# 設定無窮迴圈，讓視窗持續更新與執行
while running:
    # 從pygame事件佇列中，一項一項的檢查
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == launchMissile:
            m_x = player.xy[0] + 20
            m_y = player.xy[1]
            Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
            m_x = player.xy[0] + 80
            Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))

        if event.type == createEnemy:
            Enemies.append(Enemy(playground=playground, sensitivity=movingScale))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # 'a', 'A', 左移
                keyCountX += 1
                player.to_the_left()
            if event.key == pygame.K_d:
                keyCountX += 1
                player.to_the_right()
            if event.key == pygame.K_s:
                keyCountY += 1
                player.to_the_bottom()
            if event.key == pygame.K_w:
                keyCountY += 1
                player.to_the_top()

            if event.key == pygame.K_SPACE:
                m_x = player.x + 20
                m_y = player.y
                Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
                m_x = player.x + 80
                Missiles.append(MyMissile(playground, (m_x, m_y), movingScale))  # 若未指定參數，須按照宣告順序
                pygame.time.set_timer(launchMissile, 400)  # 之後，每400 ms發射一組

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

            if event.key == pygame.K_SPACE:
                pygame.time.set_timer(launchMissile, 0)  # 停止發射

    screen.blit(background, (0, 0))  # 更新背景圖片

    player.collision_detect(Enemies)
    for m in Missiles:
        m.collision_detect(Enemies)

    for e in Enemies:
        if e.collided:
            Boom.append(Explosion(e.center))

    Missiles = [item for item in Missiles if item.available]
    for m in Missiles:
        m.update()
        screen.blit(m.image, m.xy)

    Enemies = [item for item in Enemies if item.available]
    for e in Enemies:
        e.update()
        screen.blit(e.image, e.xy)

    # 添加player圖片
    player.update()
    screen.blit(player.image, player.xy)
    # 爆炸效果在player之上
    Boom = [item for item in Boom if item.available]
    for e in Boom:
        e.update()
        screen.blit(e.image, e.xy)

    pygame.display.update()  # 更新螢幕狀態
    dt = clock.tick(fps)  # 每秒更新fps次，This method should be called once per frame.
pygame.quit()  # 關閉繪圖視窗
