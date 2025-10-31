import random
import pygame
import alien
import importlib
#screen
background = [r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\草地_background.jpg",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\森林_background.png",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\尚水——background。PNG.png",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\盛林_BACKGROUND.png",
              r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\image\异世界_background.png"]
music = [r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\sound\一个简单的灵感循环_耳聆网_[声音ID：20111].wav",
          r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\sound\Vibrant Adventures (Uplifting Melodies for Adventure Videos)_耳聆网_[声音ID：42359].mp3"]


#ship
ship_bullet_power = [1,1,1,2,1,5,2]
ship_bullet_speed = [20,15,30,10,20,5,15]
ship_moving_speed = [7,10,7,15,7,7,7]
ship_blood = [3,3,3,3,3,3,3] 
class Settings:
    def __init__(self):
        """initialize the settings of the game"""
        #settings of the screen
        self.background_type = 4     
        self.background = pygame.image.load(background[self.background_type])
        self.background_rect = self.background.get_rect()
        self.screen_width = self.background_rect.width
        self.screen_height = self.background_rect.height
        self.bg_color = (0,220,200)

        #settings of the music and sound
        self.background_music = pygame.mixer.Sound(music[1])
        self.background_music.set_volume(1)
        self.background_music.play(-1)

        #the sound of the collisions between alien and ship
        self.ship_alien_collision_sound = pygame.mixer.Sound(r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\sound\一个盾牌敲击的声音_耳聆网_[声音ID：11002].wav")
        self.ship_alien_collision_sound.set_volume(0.7)

        #the sound about the failure
        self.fail_sound = pygame.mixer.Sound(r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\sound\一个不祥的和弦_耳聆网_[声音ID：18108].wav")
        self.fail_sound.set_volume(1)


        #settings of the ship
        self.ship_type = random.randint(0,6)
        self.ship_speed = ship_moving_speed[self.ship_type]
        self.ship_blood = ship_blood[self.ship_type]

        
        #the settings of the bullet
        self.bullet_speed = ship_bullet_speed[self.ship_type]
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (70,100,100)
        self.bullet_allowed = 20
        self.bullet_range = 400
        self.bullet_sound_volume = 0.2
        self.bullet_power = ship_bullet_power[self.ship_type]  

        #the settings of the alien
        self.alien_type = random.randint(0,5)
        self.alien_blood = 3
        self.alien_speed = 1

        #about the level
        self.speedup_scale = 1.2
       
    def initialize_dynamic_settings(self):
        """initialize the dynamic settings"""
        self.ship_speed = self.ship_speed = ship_moving_speed[self.ship_type]
        self.bullet_speed = ship_bullet_speed[self.ship_type]
        importlib.reload(alien)
        

    def increase_speed(self):
        """increase the level"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        alien.alien_speed = [speed*self.speedup_scale for speed in alien.alien_speed]


        
