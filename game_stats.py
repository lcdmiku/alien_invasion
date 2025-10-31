class GameStats:
    """track the statistics of the game"""
    def __init__(self,ai_game):
       """initialize the statistics of the game"""
       self.settings = ai_game.settings
       self.reset_stats()
       #history record
       self.highest_score = 0
       

    def reset_stats(self):
        """initialize the information"""
        self.ship_leftblood = self.settings.ship_blood
        self.score = 0
        self.game_level = 0
        self.settings.initialize_dynamic_settings()

    
    def update_his_score(self,score):
        """update the highest score"""
        if score > self.highest_score:
            self.highest_score = score
            print("congratulations!you break the record!!!")


