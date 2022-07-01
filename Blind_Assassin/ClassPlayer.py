
# BLIND ASSASSIN

# PLAYER CLASS

import pygame

class Player():
    def __init__(self,num,name):
        self.number = self.set_number(num)
        self.name = self.set_name(name)
        self.is_death = False
        self.balls = 0
        self.max_energy = 0
        self.max_moves = 0
        self.rem_energy = 0
        self.rem_moves = 0
        self.position = [0,0]

    def __str__(self):
        return ("Player %i / %s" %(self.number,self.name))

    def set_number(self,num):
        return num

    def set_name(self,name):
        return name

    def move(self,new_pos):
        self.position = new_pos

    def earn_ball(self):
        self.balls += 1

    def loose_balls(self):
        self.balls = 0

    #def deploy_player(self):
        
