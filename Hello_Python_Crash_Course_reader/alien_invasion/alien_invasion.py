import pygame
from pygame.sprite import Group

import game_functions
from alien import Alien
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    pygame.display.set_caption("Alien Invasion")

    bullets = Group()
    alien = Alien(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        game_functions.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        game_functions.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
