
"""

BLIND ASSASSIN

MAIN FILE

--- CODES ---

0 = EMPTY
1 = WALL
[2,x] = PLAYER
3 = BALL
[9,x] = ESPECIAL

"""

#------------------------------ IMPORTS

import pygame, sys, random
from pygame.locals import *

import ClassPlayer
import GridDistribution as GD

pygame.init()

#------------------------------ CONTROL CONSTANTS

MOUSE_LEFT = 1 # by default
MOUSE_RIGHT = 3 # by default

map_W = 0
map_H = 0

screen_W = 800 #1280
screen_H = 600 #704

# MARGIN = 25
TOP_MARGIN = 100

BOX_SIZE = 50

INIT_CAMERA = (0,0)

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GRAY  = (128,128,128)

#------------------------------ INIT/SET/EXIT FUNCTIONS

def init_game():
    Num_of_Players = 3 # --- NUM OF PLAYERS ---
    Name_of_Players = ['BLDR','Ojka','Coca'] # --- NAME OF PLAYERS ---
    Num_of_Balls = 5 # --- NUM OF BALLS ---
    game.set_players(Num_of_Players, Name_of_Players)
    game.set_balls(Num_of_Balls)
    game.who_starts()

def set_board():
    board_list = ['20x20_test']
    m = board_list[0] # --- SELECT MAP ---
    return m

def generate_grid(rect,box_size,board):
    grid = []
    size = [rect.get_width()/box_size,rect.get_height()/box_size]
    grid = [[0 for i in range(size[0])] for j in range(size[1])]
    walls = GD.get_distr(board)
    for w in walls:
        r = w[0]
        c = w[1]
        grid[r][c] = 1
    return grid
    

"""
def set_music():
    music_list = []
    m = random.randint(0,len(music_list)-1)
    return music_list[m]
"""

def exit_game():
    pygame.quit()
    sys.exit()

#------------------------------ MAIN LOOP

def main():
    init_game()
    
    while True:        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                exit_game()
            elif event.type == KEYUP and event.key == K_UP:
                pass
            elif event.type == KEYUP and event.key == K_DOWN:
                pass
            elif event.type == KEYUP and event.key == K_LEFT:
                pass
            elif event.type == KEYUP and event.key == K_RIGHT:
                pass
            elif event.type == KEYUP and event.key == K_SPACE:
                game.next_player()

        go()
            

#------------------------------ GAME CLASS

class Game:
    def __init__(self):
        self.PLAYERS = []
        self.BALLS = 0
        self.actual_player = None

    def set_players(self,num,name):
        for n in range(0,num):
            player = ClassPlayer.Player(n+1,name[n])
            game.PLAYERS.append(player)

    def set_balls(self,num):
        self.BALLS = num

    def who_starts(self):
        self.actual_player = random.randint(1,len(self.PLAYERS))

    def next_player(self):
        self.actual_player += 1
        self.actual_player = self.actual_player % (len(self.PLAYERS))
        if self.actual_player == 0:
            self.actual_player = len(self.PLAYERS)
        screen.fill(BLACK) #hidding stop between players
        player_info = font.render('%s'
                                  %(self.PLAYERS[self.actual_player-1].name), True, WHITE)
        screen.blit(player_info, player_info_pos)
        pygame.display.update()
        pygame.time.wait(500)

            

#------------------------------ CAMERA CLASS

class Camera:
    def __init__(self):
        self.X = INIT_CAMERA[0]
        self.Y = INIT_CAMERA[1]

    #def update(self,direction):

#------------------------------ MAIN FUNCTION

def go():
    run_game()
    blit()
    pygame.display.update()

#------------------------------ BLIT FUNCTION

def blit():
    screen.fill(WHITE)
    screen.blit(board_graph,(0,TOP_MARGIN))

    player_info = font.render('E %s/%s | M %s/%s'
                              %(game.PLAYERS[game.actual_player-1].rem_energy,
                                game.PLAYERS[game.actual_player-1].max_energy,
                                game.PLAYERS[game.actual_player-1].rem_moves,
                                game.PLAYERS[game.actual_player-1].max_moves), True, BLACK)
    screen.blit(player_info, player_info_pos)

#------------------------------ RUN GAME FUNCTION

def run_game():
    pass

#------------------------------ SET AND UPLOAD

if True:
    game = Game()
    camera = Camera()

    screen = pygame.display.set_mode((screen_W,screen_H),0,32)
    #screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    #screen_W = screen.get_width()
    #screen_H = screen.get_height()
    pygame.display.set_caption("BLIND ASSASSIN (Beta)")
    #pygame.display.set_icon(pygame.image.load('...

    board = set_board()
    board_graph = pygame.image.load('boards\\%s.jpg' %board).convert()
    grid = generate_grid(board_graph,BOX_SIZE,board)
    
    font = pygame.font.Font(None,36)
    player_info = font.render(None, True, BLACK)
    player_info_pos = (screen_W/2-80,36)

#------------------------------ EXECUTE

if __name__ == '__main__':
    main()
