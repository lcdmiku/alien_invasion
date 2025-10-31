import sys
import pygame
import random
from time import sleep
from game_stats import GameStats
from setting import Settings
from ship import Ship,image_ship
from bullet import Bullet 
from alien import Alien,Boss
from botton import Botton
from scoreboard import Scoreboard

class AlienInvasion:
    """manage the game's resourse and behavior"""
    def __init__(self):
        """initialize the game and build game resourse"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.ship = Ship(self)
        
        self.scoreboard = Scoreboard(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.bosses = pygame.sprite.Group()
        
        #pause
        self.game_active = False
        self.play_botton = Botton(self,"PLAY",self.screen_rect.center)
        self.level_1_botton = Botton(self,"Level 1",(self.screen_rect.centerx,self.screen_rect.centery-100))
        self.level_2_botton = Botton(self,"Level 2",(self.screen_rect.centerx-320,self.screen_rect.centery))
        self.level_3_botton = Botton(self,"Level 3",(self.screen_rect.centerx+320,self.screen_rect.centery))
        self._update_screen()
        #draw botton
                
         
    def run_game(self):
        """start the main circle of the game"""
        while True:
            #check the event of keyboard and mouse
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                #delete invisable bullets         
            self._update_screen()
            self.clock.tick(60)

    def _update_bullets(self):
        self.bullets.update()
        self.del_bullet()
        self._check_bullet_aliens_collisions()

    def _check_bullet_aliens_collisions(self):
        #check hit
        # if hit,delete
        self.blood_reduce_bullets(self.aliens)
        #boss case
        self.blood_reduce_bullets(self.bosses)
        if not self.aliens and not self.bosses:
            self.bullets.empty()
            #if the game has start for at least a loop,it's time to speed up
            if self.stats.score:
                self.stats.game_level += 1
                self.settings.increase_speed()
            self._create_fleet()
            self.ship.center_ship()
        #check the collisions of ship and alien

    def blood_reduce_bullets(self,aliens_group):
        """tackle the blood_reduce when bullets hit aliens"""
        collisions = pygame.sprite.groupcollide(self.bullets,aliens_group,True,False)
        if collisions:
            for bullet in collisions:
                aliens = collisions[bullet]
                for alien in aliens:
                    alien.left_blood -= self.settings.bullet_power
                    #check if alien is dead
                    if alien.left_blood <= 0:
                        self.aliens.remove(alien)
                        self.bosses.remove(alien)
                        self.stats.score += alien.blood


    def _update_aliens(self):
        """update the pos of all the aliens"""
        self.aliens.update()
        self.bosses.update() 
        self._check_aliens_ship_collisions()

    def blood_reduce_ship(self,collisions,str):
        """tackle the ship's blood_reduce when ship hit aliens"""
        if collisions:
            for alien in collisions:
                if alien.attack_able():                
                    self.stats.ship_leftblood -= alien.damage
                    self.settings.ship_alien_collision_sound.play()
                    print(f"{str}(your blood:{self.stats.ship_leftblood})")

    def _check_aliens_ship_collisions(self):
        """respond to the collisions between aliens and ship"""
        #check the collisions of ship and alien
        collisions = pygame.sprite.spritecollide(self.ship,self.aliens,False)
        collisions_boss = pygame.sprite.spritecollide(self.ship,self.bosses,False)
        self.blood_reduce_ship(collisions,"Ship hit!!!")
        #boss track
        self.blood_reduce_ship(collisions_boss,"Attacked by boss!!!")
            
        if self.stats.ship_leftblood <= 0:
            #music update
            self.settings.fail_sound.play()
            self.restart()
            #pause
            self.game_active = False
            pygame.mouse.set_visible(not self.game_active)

    def restart(self):
        """to restart the game"""
        print(f"game over!your score:{self.stats.score}")
        #update
        self.stats.update_his_score(self.stats.score)           
        self.bosses.empty()
        self.bullets.empty()
        self.aliens.empty()
        self.ship.center_ship()
        self.stats.reset_stats()

    def _check_events(self):
        """respond to the event"""
        for event in pygame.event.get():           
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.game_active:
                    self._check_play_botton(mouse_pos)
                    self._check_level_botton(mouse_pos)

    
    def _check_play_botton(self,mouse_pos):
        """when hit the play_botton,start the game"""
        if self.play_botton.rect.collidepoint(mouse_pos):
            self.game_active = True
            pygame.mouse.set_visible(not self.game_active)

    def _check_level_botton(self,mouse_pos):
        """when hit the level botton,interact"""
        count = 0
        if self.level_1_botton.rect.collidepoint(mouse_pos):
            count = 1
        if self.level_2_botton.rect.collidepoint(mouse_pos):
            count = 2
        if self.level_3_botton.rect.collidepoint(mouse_pos):
            count = 3
        self.stats.game_level = count
        self.settings.initialize_dynamic_settings()
        for i in range(0,count):
            self.settings.increase_speed()
        if count:
            self.game_active = True
            pygame.mouse.set_visible(not self.game_active)
        



    def _check_keydown_events(self,event):
        """respond to keydown"""
        if event.key == pygame.K_d:
            #move the spaceship to right
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            #move the spaceship to left
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            #move the space up
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            #move the spaceship down
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            #quit
            sys.exit()
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #fire 
            self._fire_bullet(event.key)
        elif event.key == pygame.K_c:
            #change your ship
            self.settings.ship_type = random.randint(0,6)
            self.image = pygame.image.load(image_ship[self.settings.ship_type])
            self.rect = self.image.get_rect()
        elif event.key == pygame.K_p:
            #pause
            self.game_active = not self.game_active
            pygame.mouse.set_visible(not self.game_active)
    
    def _check_keyup_events(self,event):
        """respond to keyup"""
        if event.key == pygame.K_d:
            #stop moving to right
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            #stop moving to left
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            #stop moving the space up
            self.ship.moving_up = False

        elif event.key == pygame.K_s:
            #stop moving the spaceship down
            self.ship.moving_down = False

    def _update_screen(self):
        """update the screen"""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.background,self.screen.get_rect())
        for bullet in self.bullets:
            bullet.draw_bullet() 
        #make the screen visable
        self.ship.blitme()
        for boss in self.bosses:
            boss.draw_blood_bar()
        self.bosses.draw(self.screen)
        self.aliens.draw(self.screen)       
        #display the board
        self.scoreboard.show_board()
        
        #if not gameactive,draw play_botton
        if not self.game_active:
            
            self.level_1_botton.draw_botton()
            self.level_2_botton.draw_botton()
            self.level_3_botton.draw_botton()
            self.play_botton.draw_botton()
        pygame.display.flip()

    def _fire_bullet(self,key):
        """build a bullet"""
        if len(self.bullets) < self.settings.bullet_allowed and self.game_active :
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            if key == pygame.K_RIGHT:
                new_bullet.right = True
            if key == pygame.K_LEFT:
                new_bullet.left = True
            if key == pygame.K_UP:
                new_bullet.up = True
            if key == pygame.K_DOWN:
                new_bullet.down = True
    
    def del_bullet(self):
        for bullet in self.bullets:
            #check screen's barrier
            if bullet.rect.bottom <= 0 or bullet.rect.top >= self.settings.screen_height or bullet.rect.right <= 0 or bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
            if bullet.del_able:
                self.bullets.remove(bullet)
    
    #the def about alien
    def _create_fleet(self):
        """build a new alien"""
        boss = Boss(self)
        self.bosses.add(boss)       
        current_x = 0
        while current_x < self.settings.screen_width:
            self._create_alien(current_x,random.randint(0,100))
            current_x += 200
            
    def _create_alien(self,x_position,y_position):
        """build a alien and put it in place"""
        new_alien = Alien(self)
        if x_position+new_alien.rect.width > self.settings.screen_width:
            x_position = self.settings.screen_width - new_alien.rect.width
        new_alien.x = x_position
        new_alien.y = y_position  
        self.aliens.add(new_alien)
        

if __name__ == '__main__':
    #build the game and run
    ai = AlienInvasion()
    ai.run_game()