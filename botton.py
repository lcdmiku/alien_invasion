import pygame.font
class Botton:
    """build bottons"""
    def __init__(self,ai_game,msg,pos):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #set the size and other attributes of the bottons
        self.width,self.height = 200,50
        self.botton_color = (100,0,100)
        self.text_color = (0,250,255)
        self.font = pygame.font.SysFont(r"C:\Users\lcd\Desktop\python_work\alien_invasion\res\font\FangZhengDaBiaoSong-GBK-1.ttf",48)

        #build the rect of the botton and put it at the center
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #render the text
        self.prep_msg(msg,pos)
        

    def prep_msg(self,msg,pos):
        """render the msg and put the text at the center of the botton"""
        self.msg_image = self.font.render(msg,True,self.text_color,self.botton_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = pos 
        self.rect.center = pos

    def draw_botton(self):
        """draw a botton filled with color and then draw the text"""
        self.screen.fill(self.botton_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)



        