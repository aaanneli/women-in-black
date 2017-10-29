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
        self.x = random.randint(room.rect.center[0] - room.getWidth() // 4, room.rect.center[0] + room.getWidth() // 4)
        self.y = random.randint(room.rect.center[1] - room.getHeight() // 4, room.rect.center[1] + room.getHeight() // 4)
        self.room = room
        self.width = KEY_WIDTH
        self.height = KEY_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
