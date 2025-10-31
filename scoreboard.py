import pygame
from heart import Heart
from pygame.sprite import Group

font_type = [r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\font\FangZhengDaBiaoSong-GBK-1.ttf"]
class Scoreboard:
    """display the score and any other information"""

    def __init__(self,ai_game):
        """initialize the attribuutes of the score"""
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #the font of displaying
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(font_type[0],48)

        #prepare the initial picture
        self.prep_score()


    def prep_score(self):
        """render the score"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color)

        #display the score at the right top
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """render the level"""
        level_str = str(self.stats.game_level)
        self.level_image = self.font.render(level_str,True,self.text_color)
        #display the level under the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.midtop = self.score_rect.midbottom

    def prep_record(self):
        """render the record"""
        record_str = str(self.stats.highest_score)
        self.record_imgage = self.font.render(record_str,True,self.text_color)
        #display the record under the level
        self.record_rect = self.record_imgage.get_rect()
        self.record_rect.midtop = self.level_rect.midbottom

    def prep_hearts(self):
        """render hp"""
        self.hearts = Group()
        for ship_blood in range(self.stats.ship_leftblood):
            heart = Heart(self.ai_game)
            heart.rect.x = 10 + ship_blood * heart.rect.width
            heart.rect.y = 10
            heart.add(self.hearts)



    def show_board(self):
        """display the board"""
        self.prep_score()
        self.prep_level()
        self.prep_record()
        self.prep_hearts()
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.screen.blit(self.record_imgage,self.record_rect)
        self.hearts.draw(self.screen)