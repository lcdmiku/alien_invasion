import pygame
from pygame.sprite import Sprite
import random
import time

alien_image = [r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\胡桃[漫幻家]   原神角色人物立绘PNG透明底图片素材-小图_爱给网_aigei_com.png",
               r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\泳装祭 甘雨   原神角色人物立绘PNG透明底图片素材_爱给网_aigei_com.png",
               "C:\\Users\\lcd\\Desktop\\python_work\\alien_invasion\\res\image\\妮露 立绘图2   原神角色人物立绘PNG透明底图片素材-小图_爱给网_aigei_com.png",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\red_dragon.png",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\流浪者 立绘2[漫幻家]   原神角色人物立绘PNG透明底图_爱给网_aigei_com.png",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\旅行者 荧[漫幻家]   原神角色人物立绘PNG透明底图片素-小图_爱给网_aigei_com.png",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\frame-2.png"]

alien_blood = [1,10,3,1,3,3]
alien_speed = [6,0.5,5,7,5,5]
alien_damage = [1,1,1,1,1,1]

boss_speed = [6,1,1,1,1,1,2]
boss_blood = [10,20,10,10,10,10,30]
boss_damage = [2,2,2,2,2,2,2]



class Alien(Sprite):
    """simulate a alien"""
    def __init__(self, ai_game):
        """initialize the alien and its initial position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship = ai_game.ship        
        self.screen_rect = ai_game.screen.get_rect()

        #the attributes of the alien
        self.alien_type = (random.randint(0,5))
        self.blood = alien_blood[self.alien_type]
        self.left_blood = self.blood
        self.speed = alien_speed[self.alien_type]
        self.damage = alien_damage[self.alien_type]
        #attack 
        self.last_attack_time = 0
        self.attack_interval = 2

        self.moving_dir_x = 0
        self.moving_dir_y = 0

        self.one_dir_time = 30
        self.clock = self.one_dir_time

        #load down the image of the alien and set the attributes of their rects
        self.image = pygame.image.load(alien_image[self.alien_type])
        self.rect = self.image.get_rect()
        
        #each alien will show up at the left_up corner
        self.rect.x = 0
        self.rect.y = 0 

        #store the exact position of the alien
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """update the position of the alien"""
        
        if self.clock == self.one_dir_time:
            self.moving_dir_x = random.randint(0,2)
            self.moving_dir_y = random.randint(0,2)
            self.clock = 0
        else :
            self.clock += 1
                   
        if self.moving_dir_y == 0 and self.rect.bottom <= self.settings.screen_height:
            self.y += self.speed
        if self.moving_dir_x == 0 and self.rect.right <= self.settings.screen_width:
            self.x += self.speed
        if self.moving_dir_x == 1 and self.rect.left >= 0:
            self.x -= self.speed
        if self.moving_dir_y == 1 and self.rect.top >= 0:
            self.y -= self.speed
            
        self.rect.x = self.x
        self.rect.y = self.y

    def attack_able(self):
        """judge if the alien can attack again"""
        if time.time() - self.last_attack_time >= self.attack_interval:
            self.last_attack_time = time.time()
            return True
        else :
            return False
        


class Boss(Alien):
    """simulate the boss of the aliens"""
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.alien_type = 6
        #the attributes of the alien
        self.blood = boss_blood[self.alien_type]
        self.left_blood = self.blood
        self.speed = boss_speed[self.alien_type]
        self.damage = boss_damage[self.alien_type]

        #pos random
        self.x = random.randint(0,self.settings.screen_width)

        #load down the image of the alien and set the attributes of their rects
        self.image = pygame.image.load(alien_image[self.alien_type])
        self.rect = self.image.get_rect()

        #the boss's reaction rate
        self.one_dir_time = 15
        self.clock = self.one_dir_time

        #the boss's blood_bar
        self.blood_bar_width = 900
        self.blood_bar_height = 50
        self.blood_bar_rect = pygame.Rect(0,50,self.blood_bar_width,self.blood_bar_height)
        self.blood_bar_rect.centerx = self.screen_rect.centerx
        


    def update(self):
        """want the boss to chase the ship"""
        if self.clock == self.one_dir_time:
            self.clock = 0
            if self.rect.x < self.ship.rect.x:
                self.moving_dir_x = 0
            elif self.rect.x > self.ship.rect.x:
                self.moving_dir_x = 1
            else :
                self.moving_dir_x = 2
            if self.rect.y < self.ship.rect.y:
                self.moving_dir_y = 0
            elif self.rect.y > self.ship.rect.y :
                self.moving_dir_y = 1
            else :
                self.moving_dir_y = 2
        else:
            self.clock += 1
            

        if self.moving_dir_y == 0 and self.rect.bottom <= self.settings.screen_height:
            self.y += self.speed
        if self.moving_dir_x == 0 and self.rect.right <= self.settings.screen_width:
            self.x += self.speed
        if self.moving_dir_x == 1 and self.rect.left >= 0:
            self.x -= self.speed
        if self.moving_dir_y == 1 and self.rect.top >= 0:
            self.y -= self.speed
            
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_blood_bar(self):
        """draw the blood_bar for the boss"""
        self.blood_bar_rect.width = self.blood_bar_width * self.left_blood / self.blood
        pygame.draw.rect(self.screen,(255,0,0),self.blood_bar_rect)



