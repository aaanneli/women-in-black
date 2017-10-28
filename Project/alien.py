import pygame, sys
from pygame.locals import *
from player import *
from constant import *


class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y, *groups):
        super(Alien,self).__init__(*groups)
        self.images = []
        self.index = 0
        self.direction = RIGHT
        self.image = self.images[self.direction][self.index]
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def walkUp(self):
        if self.direction != UP:
            self.direction = UP
        self.rect.y -= MOVING_INDEX 
        self.image = self.images[UP][self.index]
        self.index = (self.index + 1) % len(self.images[UP])

    def walkDown(self):
        if self.direction != DOWN:
            self.direction = DOWN
        self.rect.y += MOVING_INDEX 
        self.image = self.images[DOWN][self.index]
        self.index = (self.index + 1) % len(self.images[DOWN])


    def walkRight(self):
        if self.direction != RIGHT:
            self.direction = RIGHT
        self.rect.x += MOVING_INDEX 
        self.image = self.images[RIGHT][self.index]
        self.index = (self.index + 1) % len(self.images[RIGHT])

    def walkLeft(self):
        if self.direction != LEFT:
            self.direction = LEFT
        self.rect.x -= MOVING_INDEX 
        self.image = self.images[LEFT][self.index]
        self.index = (self.index + 1) % len(self.images[LEFT])
