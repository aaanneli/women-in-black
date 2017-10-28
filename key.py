import pygame, sys
from pygame.locals import *
from constant import *
import random

x_upper_lim = SCREEN_WIDTH
x_lower_lim = 0

y_upper_lim = SCREEN_HEIGHT
y_lower_lim = 0

class Key(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Key, self).__init__(*groups)
        self.image = pygame.image.load('pics/key.png')
        self.index = 0
        self.x = random.randint(x_lower_lim, x_upper_lim)
        self.y = random.randint(y_lower_lim, y_upper_lim)
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

