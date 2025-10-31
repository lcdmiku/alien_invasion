
import pygame
import random
image_ship = ["C:/Users/lcd/Desktop/python_work/alien_invasion/res/image/spiked ship 3. small.blue_.PNG",
              "C:/Users/lcd/Desktop/python_work/alien_invasion/res/image/spiked ship 3. small.green_.PNG",
              "C:/Users/lcd/Desktop/python_work/alien_invasion/res/image/spiked ship 3. small.PNG",
              "C:\\Users\\lcd\\Desktop\\python_work\\alien_invasion\\res\image\\妮露 立绘图2   原神角色人物立绘PNG透明底图片素材-小图_爱给网_aigei_com.png",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\red_dragon.png",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\流浪者 立绘2[漫幻家]   原神角色人物立绘PNG透明底图_爱给网_aigei_com.png",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\旅行者 荧[漫幻家]   原神角色人物立绘PNG透明底图片素-小图_爱给网_aigei_com.png"]

Ship_power = [1,1,1,2,1,3,2]
class Ship:
    """manage the ships"""
    def __init__(self,ai_game):
        """initialize the ships and their first location"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.stats = ai_game.stats
        
        #the attributes of ship
        self.blood = self.settings.ship_blood
        

        #load down the image of the ships 
        self.image = pygame.image.load(image_ship[self.settings.ship_type])
        self.rect = self.image.get_rect()

        #each ship will be placed at the middle of the botten of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #moving mark
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #the ship's blood_bar
        self.blood_bar_width = 900
        self.blood_bar_height = 50
        self.blood_bar_rect = pygame.Rect(0,50,self.blood_bar_width,self.blood_bar_height)
        self.blood_bar_rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """picture the ships at pointed positions"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """adjust the position of the spaceship accordding to the moving mark"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        #update the rect
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """put the ship at the midbottom"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw_blood_bar(self):
        """draw the blood_bar for the ahip"""
        self.blood_bar_rect.width = self.blood_bar_width * self.stats.ship_leftblood / self.blood
        pygame.draw.rect(self.screen,(0,250,0),self.blood_bar_rect)
