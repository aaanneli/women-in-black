import pygame, sys
from pygame.locals import *
from player import *
from constant import *


class Boss(pygame.sprite.Sprite):
    def __init__(self,x,y, *groups):
        super(Boss,self).__init__(*groups)
        self.images = [[] for i in range(NUMBER_OF_DIRECTION)]
        for i in range(3):
            self.images[UP].append(pygame.image.load('pics/boss/up'+str(i)+'.png'))
            self.images[LEFT].append(pygame.image.load('pics/boss/left'+str(i)+'.png'))
            self.images[DOWN].append(pygame.image.load('pics/boss/down'+str(i)+'.png'))
            self.images[RIGHT].append(pygame.image.load('pics/boss/right'+str(i)+'.png'))
        self.index = 0
        self.direction = DOWN
        self.image = self.images[self.direction][self.index]
        self.x = x
        self.y = y
        self.width = BOSS_WIDTH
        self.widthAlt = BOSS_WIDTH_ALT
        self.height = BOSS_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.countStep = 0
        self.life = 3

    def walkUp(self):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
        self.direction = UP
        self.rect.y -= BOSS_MOVING_INDEX 
        self.image = self.images[UP][self.index]
        self.index = (self.index + 1) % len(self.images[UP])

    def walkDown(self):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
        self.direction = DOWN
        self.rect.y += BOSS_MOVING_INDEX 
        self.image = self.images[DOWN][self.index]
        self.index = (self.index + 1) % len(self.images[DOWN])


    def walkRight(self):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.widthAlt, self.height)
        self.direction = RIGHT
        self.rect.x += BOSS_MOVING_INDEX 
        self.image = self.images[RIGHT][self.index]
        self.index = (self.index + 1) % len(self.images[RIGHT])

    def walkLeft(self):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.widthAlt, self.height)
        self.direction = LEFT
        self.rect.x -= BOSS_MOVING_INDEX 
        self.image = self.images[LEFT][self.index]
        self.index = (self.index + 1) % len(self.images[LEFT])

    def update(self,dt,game):
        if (self.life > 0):
            player2 = game.player2.rect
            xDiff = player2.x - self.rect.x
            yDiff = player2.y - self.rect.y
            if (abs(xDiff) > abs(yDiff)):
                if xDiff > 0:
                    self.walkRight()
                else:
                    self.walkLeft()
            else:
                if yDiff > 0:
                    self.walkDown()
                else:
                    self.walkUp()
            if self.rect.colliderect(game.player1.rect) or self.rect.colliderect(player2):
                game.isPlaying = False
            pygame.draw.rect(game.screen, GREEN, pygame.Rect((self.rect.x, self.rect.y - 10), (self.width / 3 * self.life, 10)))
        
            
