import pygame, sys
from pygame.locals import *
from constant import *
import random

x_upper_lim = SCREEN_WIDTH
x_lower_lim = 0

y_upper_lim = SCREEN_HEIGHT
y_lower_lim = 0

class Key(pygame.sprite.Sprite):
    def __init__(self, room, *groups):
        super(Key, self).__init__(*groups)
        self.image = pygame.image.load('pics/key.png')
        self.x = random.randint((room.topLeft[1]*TILE_WIDTH)+15, (room.bottomRight[1]* TILE_WIDTH)-15)
        self.y = random.randint((room.topLeft[0]*TILE_HEIGHT)+15, (room.bottomRight[0]*TILE_HEIGHT)-15)
        self.room = room
        self.width = 50
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
