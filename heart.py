import pygame
from pygame.sprite import Sprite

class Heart(Sprite):
    """simulate the hp of the ship by hearts"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats
        self.image = pygame.image.load(r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\像素游戏2D素材 (4)-游戏道具地图房子建筑超级玛丽_爱给网_aigei_com.png")
        self.rect = self.image.get_rect()
