import pygame, sys
from pygame.locals import *
from player import *
from constant import *


class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y, *groups):
        super(Alien,self).__init__(*groups)
        self.images = [[] for i in range(NUMBER_OF_DIRECTION)]
        for i in range(3):
            self.images[UP].append(pygame.image.load('pics/alien1/up'+str(i)+'.png'))
            self.images[LEFT].append(pygame.image.load('pics/alien1/left'+str(i)+'.png'))
            self.images[DOWN].append(pygame.image.load('pics/alien1/down'+str(i)+'.png'))
            self.images[RIGHT].append(pygame.image.load('pics/alien1/right'+str(i)+'.png'))
        self.index = 0
        self.direction = DOWN
        self.image = self.images[self.direction][self.index]
        self.x = x
        self.y = y
        self.width = 20
        self.height = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.countStep = 0

    def walkUp(self):
        self.direction = UP
        self.rect.y -= ALIEN_MOVING_INDEX 
        self.image = self.images[UP][self.index]
        self.index = (self.index + 1) % len(self.images[UP])

    def walkDown(self):
        self.direction = DOWN
        self.rect.y += ALIEN_MOVING_INDEX 
        self.image = self.images[DOWN][self.index]
        self.index = (self.index + 1) % len(self.images[DOWN])


    def walkRight(self):
        self.direction = RIGHT
        self.rect.x += ALIEN_MOVING_INDEX 
        self.image = self.images[RIGHT][self.index]
        self.index = (self.index + 1) % len(self.images[RIGHT])

    def walkLeft(self):
        self.direction = LEFT
        self.rect.x -= ALIEN_MOVING_INDEX 
        self.image = self.images[LEFT][self.index]
        self.index = (self.index + 1) % len(self.images[LEFT])

    def update(self,dt,game):
        player2 = game.player2.rect
        
        isWallCollide = False
        positionBetweenWall = ""
        for wall in game.walls:
            if self.rect.colliderect(wall):
                isWallCollide = True
                positionBetweenWall += checkPositionBetweenWall(wall,self.rect)

        if getDistance(self.rect,player2) > ALIEN_SAFE_DISTANCE:
            if self.direction == UP:
                if not (isWallCollide and "top" in positionBetweenWall):
                    self.walkUp()
            elif self.direction == LEFT:
                if not (isWallCollide and "left" in positionBetweenWall):
                    self.walkLeft()
            elif self.direction == RIGHT:
                if not (isWallCollide and "right" in positionBetweenWall):
                    self.walkRight()
            elif self.direction == DOWN:
                if not (isWallCollide and "below" in positionBetweenWall):
                    self.walkDown()
            self.countStep += 1
            if(self.countStep > ALIEN_RANDOM_STEP):
                self.countStep = 0
                self.direction = (self.direction + 1) % NUMBER_OF_DIRECTION
        else:
            xDiff = player2.x - self.rect.x
            yDiff = player2.y - self.rect.y
            if (abs(xDiff) > abs(yDiff)):
                if xDiff > 0:
                    if not (isWallCollide and "right" in positionBetweenWall):
                        self.walkRight()
                else:
                    if not (isWallCollide and "left" in positionBetweenWall):
                        self.walkLeft()
            else:
                if yDiff > 0:
                    if not (isWallCollide and "below" in positionBetweenWall):
                        self.walkDown()
                else:
                    if not (isWallCollide and "top" in positionBetweenWall):
                        self.walkUp()
        if self.rect.colliderect(game.player1.rect) or self.rect.colliderect(player2):
            #game.isPlaying = False
            pass
            
