import pygame, sys
from pygame.locals import *
from constant import *
from key import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super(Player, self).__init__(*groups)
        self.images = [[] for x in range(4)]
        self.index = 0
        self.direction = RIGHT
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self,dt,game):
        pass

    def walkUp(self):
        self.direction = UP
        self.rect.y -= MOVING_INDEX 
        self.image = self.images[UP][self.index]
        self.index = (self.index + 1) % len(self.images[UP])

    def walkDown(self):
        self.direction = DOWN
        self.rect.y += MOVING_INDEX 
        self.image = self.images[DOWN][self.index]
        self.index = (self.index + 1) % len(self.images[DOWN])


    def walkRight(self):
        self.direction = RIGHT
        self.rect.x += MOVING_INDEX 
        self.image = self.images[RIGHT][self.index]
        self.index = (self.index + 1) % len(self.images[RIGHT])

    def walkLeft(self):
        self.direction = LEFT
        self.rect.x -= MOVING_INDEX 
        self.image = self.images[LEFT][self.index]
        self.index = (self.index + 1) % len(self.images[LEFT])

    def useAbility(self):
        pass


class Player1(Player):
    def __init__(self, *groups):
        super(Player1, self).__init__(100,100,*groups)
        for i in range(9):
            self.images[UP].append(pygame.image.load('pics/player1/up'+str(i)+'.png'))
            self.images[LEFT].append(pygame.image.load('pics/player1/left'+str(i)+'.png'))
            self.images[DOWN].append(pygame.image.load('pics/player1/down'+str(i)+'.png'))
            self.images[RIGHT].append(pygame.image.load('pics/player1/right'+str(i)+'.png'))
        self.image = self.images[DOWN][0]

    def update(self,dt,game):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if (self.rect.colliderect(game.player2.rect)):
                print(self.rect.top, game.player2.rect.bottom)
            self.walkUp()
        if key[pygame.K_a]:
            self.walkLeft()
        if key[pygame.K_s]:
            self.walkDown()
        if key[pygame.K_d]:
            self.walkRight()

class Player2(Player):
    def __init__(self, *groups):
        super(Player2, self).__init__(200,200,*groups)
        for i in range(9):
            self.images[UP].append(pygame.image.load('pics/player1/up'+str(i)+'.png'))
            self.images[LEFT].append(pygame.image.load('pics/player1/left'+str(i)+'.png'))
            self.images[DOWN].append(pygame.image.load('pics/player1/down'+str(i)+'.png'))
            self.images[RIGHT].append(pygame.image.load('pics/player1/right'+str(i)+'.png'))
        self.image = self.images[DOWN][0]

        self.has_key = False

    def update(self,dt,game):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.walkUp()
        if key[pygame.K_LEFT]:
            self.walkLeft()
        if key[pygame.K_DOWN]:
            self.walkDown()
        if key[pygame.K_RIGHT]:
            self.walkRight()

        if self.rect.colliderect(game.key) and not self.has_key:
            self.has_key = True
            game.sprites.remove(game.key)

    
    
