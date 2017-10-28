import pygame, sys
from pygame.locals import *
from constant import *

class Key(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Key, self).__init__(*groups)
        self.image = pygame.image.load('pics/key.png')
        self.index = 0
        self.x = 100
        self.y = 100
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

