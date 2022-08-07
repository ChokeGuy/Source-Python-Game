import pygame ,sys,csv
import pandas as pd
from pygame.locals import *
from settings import *
from level import Level
from debug import debug
import data
import time
from button import Button
def writetocsv():
    thongke_data = { 
                'total_damage':round(data.total_damage,1),
                'total_damage_taken':data.total_damage_taken,
                'total_time':data.total_time,
                'exp':data.exp,
                'healing':data.healing,
                'sword':data.sword_damage,
                'lance':data.lance_damage,
                'axe':data.axe_damage,
                'rapier':data.rapier_damage,
                'sai':data.sai_damage,
                'sword_use_time':data.count_sword,
                'lance_use_time':data.count_lance,
                'axe_use_time':data.count_axe,
                'rapier_use_time':data.count_rapier,
                'sai_use_time':data.count_sai,
                }
    with open('./thongke.csv','a',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([thongke_data['total_damage'],thongke_data['total_damage_taken'],thongke_data["total_time"],thongke_data['exp'],thongke_data['healing']
                    ,thongke_data['sword'],thongke_data['lance'],thongke_data['axe'],thongke_data['rapier'],thongke_data['sai']
                    ,thongke_data['sword_use_time'],thongke_data['lance_use_time'],thongke_data['axe_use_time'],thongke_data['rapier_use_time'],thongke_data['sai_use_time']])         
class Game:
    def __init__(self): 
        #general setup   
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))             
        pygame.mouse.set_cursor(pygame.cursors.arrow)
        pygame.display.set_caption("Zelda")
        self.clock  = pygame.time.Clock()
        self.level = Level()   
        self.state = 'intro'
        self.stop_state = False
        self.sound = True
        self.restart = False
        #SOUND
        self.main_sound = pygame.mixer.Sound('./audio/main.wav')
        self.main_sound.play(loops=-1)
        self.main_sound.set_volume(0.2)
        #START MENU
    def get_font(self,size): # 
        return pygame.font.Font("./font/font.ttf",size)
    def intro(self):
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_SCREEN =  pygame.image.load("./graphics/tilemap/intro_img.jpg").convert_alpha()
        MENU_SCREEN =  pygame.transform.scale(MENU_SCREEN,(WIDTH,HEIGHT+50))
        MENU_RECT = MENU_SCREEN.get_rect(center=(WIDTH/2, HEIGHT/2))

        PLAY_BUTTON = Button(image=pygame.image.load("./button/button_play.png"), pos=(640, 250), 
                            text_input="Start Game", font=self.get_font(35), base_color="#FFFF00", hovering_color="White")
        # OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
        #                     text_input="OPTIONS", font=self.main_font.get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("./button/button_quit.png"), pos=(640, 550), 
                            text_input="Exit", font=self.get_font(35), base_color="#FFFF00", hovering_color="White")
        self.main_font = pygame.font.SysFont('arial', 60)
        self.screen.blit(MENU_SCREEN, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(self.screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):                   
                    self.state = 'main_game'
                    self.playing_time = time.time()                   
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()    
        pygame.display.update()
        self.clock.tick(FPS)
    def stopping_game(self):
        pygame.mouse.set_visible(True)
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_SCREEN =  pygame.image.load("./button/button_quit.png").convert_alpha()
        MENU_SCREEN =  pygame.transform.scale(MENU_SCREEN,(WIDTH,HEIGHT+50))
        MENU_SCREEN.set_alpha(20)
        MENU_RECT = MENU_SCREEN.get_rect(center=(WIDTH/2, HEIGHT/2))

        RESUME_BUTTON = Button(image=pygame.image.load("./button/button_play.png"), pos=(640, 250), 
                            text_input="Resume", font=self.get_font(35), base_color="#FFFF00", hovering_color="White")
        # OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
        #                     text_input="OPTIONS", font=self.main_font.get_font(75), base_color="#d7fcd4", hovering_color="White")
        EXIT_BUTTON = Button(image=pygame.image.load("./button/button_quit.png"), pos=(640, 550), 
                            text_input="Quit", font=self.get_font(35), base_color="#FFFF00", hovering_color="White")
        self.main_font = pygame.font.SysFont('arial', 60)
        self.screen.blit(MENU_SCREEN,MENU_RECT)

        for button in [RESUME_BUTTON, EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(self.screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                end_time = time.time()
                data.total_time = round((end_time - start_time),2)
                writetocsv()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS):                   
                    self.state = 'main_game'
                    self.level.toggle_menu()
                    self.continue_time = time.time()
                    self.stop_state = True
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    end_time = time.time()
                    data.total_time = round((end_time - start_time),2)
                    writetocsv()
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        self.clock.tick(FPS)
    def main_game(self):
        self.inplaying_time = time.time()
        if not self.stop_state:
            if self.inplaying_time >= self.playing_time + 0.5:
                data.playing = True
        else:
            if self.inplaying_time >= self.continue_time + 0.5:
                data.playing = True
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():         
            if event.type == QUIT:
                end_time = time.time()
                data.total_time = round((end_time - start_time),2)
                # df = pd.DataFrame(thongke_data)
                # df.to_csv('thongke.csv',index=None,header=True)
                writetocsv()
                pygame.quit()
                sys.exit()              
            if self.level.player.health < 0 or data.total_monster == 0:                
                self.state = 'outro'
                self.main_sound.set_volume(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    data.stopping = False
                    self.level.toggle_menu()
                if event.key == pygame.K_ESCAPE:
                    self.level.toggle_menu()
                    data.stopping = True
                    self.state = 'stopping_game'
                    data.playing = False
                    
        self.screen.fill(WATER_COLOR)
        self.level.run()
        
        # debug(pygame.mouse.get_pos())
        # debug(pygame.mouse.get_pressed(),40)
        pygame.display.update()
        
        self.clock.tick(FPS)
    def outro(self):
        pygame.mouse.set_visible(True)
        pygame.mouse.set_cursor(pygame.cursors.arrow)
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        if self.level.player.health < 0:
            MENU_SCREEN = self.get_font(45).render("You Lost", True, "Red")
        elif data.total_monster == 0:
            MENU_SCREEN = self.get_font(45).render("You Won", True, "Red")
        MENU_SCREEN.set_alpha(20)
        MENU_RECT = MENU_SCREEN.get_rect(center=(640, 160))

        AGAIN_BUTTON = Button(image=pygame.image.load("./button/button_play.png"), pos=(640, 350), 
                            text_input="Play Again", font=self.get_font(35), base_color="#FFFF00", hovering_color="White")
        # OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
        #                     text_input="OPTIONS", font=self.main_font.get_font(75), base_color="#d7fcd4", hovering_color="White")
        EXIT_BUTTON = Button(image=pygame.image.load("./button/button_quit.png"), pos=(640, 550), 
                            text_input="Quit", font=self.get_font(35), base_color="#FFFF00", hovering_color="White")
        self.main_font = pygame.font.SysFont('arial', 60)
        self.screen.blit(MENU_SCREEN,MENU_RECT)

        for button in [AGAIN_BUTTON, EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(self.screen)
        self.main_font = pygame.font.SysFont('arial', 80)        
        for event in pygame.event.get():
            if event.type == QUIT:
                end_time = time.time()
                data.total_time = round((end_time - start_time),2)
                pygame.quit()
                sys.exit()            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AGAIN_BUTTON.checkForInput(MENU_MOUSE_POS): 
                    self.restart = True 
                    writetocsv()                
                    self.state = 'intro'
                    data.playing = False
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    end_time = time.time()
                    data.total_time = round((end_time - start_time),2)
                    writetocsv()
                    pygame.quit()
                    sys.exit()
                
                # df = pd.DataFrame(thongke_data)
                # df.to_csv('thongke.csv',index=None,header=True)                   
        pygame.display.update()
        self.clock.tick(FPS)
    def state_manager(self) :
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'outro':
            self.outro()  
        if self.state == 'stopping_game':
            self.stopping_game()
if __name__ == '__main__':
    start_time = time.time()
    game = Game()
    while True :
        game.state_manager()
        if game.restart:
            game = Game()
            game.state_manager()
        