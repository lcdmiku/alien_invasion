import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """manage the bullet fired by the spaceship"""
    """build a bullet by the spaceship"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #build a rect at (0,0) and set it to right position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        #stored the position of the bullet by float
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.del_able = False
        #the initial pos of the bullet to achieve the range 
        self.init_x = self.x
        self.init_y = self.y
        self.right = False
        self.left = False
        self.up = False
        self.down = False

        #sound part
        self.sound = pygame.mixer.Sound(r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\sound\游戏激光武器射击_耳聆网_[声音ID：16629].wav")
        self.sound.set_volume(self.settings.bullet_sound_volume)
        self.sound.play()

    def update(self):
        """move the bullet up"""
        #update the position of the bullet
        if self.up:
            self.y -= self.settings.bullet_speed
        if self.down:
            self.y += self.settings.bullet_speed
        if self.right:
            self.x += self.settings.bullet_speed
        if self.left:
            self.x -= self.settings.bullet_speed
        #update the position of the rect
        if (self.x-self.init_x)**2+(self.y-self.init_y)**2 > self.settings.bullet_range**2:
            self.del_able = True
        self.rect.y = self.y
        self.rect.x = self.x
    
    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)



   
       
    
    