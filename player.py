import pygame, sys
from pygame.locals import *
from constant import *
from key import *
from maze import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super(Player, self).__init__(*groups)
        self.images = [[] for i in range(NUMBER_OF_DIRECTION)]
        self.index = 0
        self.direction = RIGHT
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
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
        super(Player1, self).__init__(10,10,*groups)
        for i in range(9):
            self.images[UP].append(pygame.image.load('pics/player1/up'+str(i)+'.png'))
            self.images[LEFT].append(pygame.image.load('pics/player1/left'+str(i)+'.png'))
            self.images[DOWN].append(pygame.image.load('pics/player1/down'+str(i)+'.png'))
            self.images[RIGHT].append(pygame.image.load('pics/player1/right'+str(i)+'.png'))
        self.image = self.images[DOWN][0]

    def update(self,dt,game):
        key = pygame.key.get_pressed()
        
        isPlayerCollide = self.rect.colliderect(game.player2.rect)
        positionBetween = checkPostionBetweenRect(game.player2.rect,self.rect)

        isWallCollide = False
        positionBetweenWall = ""
        for wall in game.walls:
            if self.rect.colliderect(wall):
                isWallCollide = True
                positionBetweenWall += checkPostionBetweenRect(wall,self.rect)
                break

        isDoorCollide = False
        positionBetweeDoor = ""
        for door in game.doors:
            if self.rect.colliderect(door.rect):
                if (door.open):
                    isDoorCollide = True
                    positionBetweeDoor += checkPostionBetweenRect(door.rect,self.rect)
                    break
        if key[pygame.K_w]:
            if (isWallCollide and "top" in positionBetweenWall):
                if isDoorCollide and "top" in positionBetweeDoor or "below" in positionBetweeDoor:
                    pass
                else:
                    return
            self.walkUp()
        if key[pygame.K_a]:
            if (isWallCollide and "left" in positionBetweenWall):
                if isDoorCollide and "left" in positionBetweeDoor:
                    pass
                else:
                    return
            self.walkLeft()
        if key[pygame.K_s]:
            if (isWallCollide and "below" in positionBetweenWall):
                if isDoorCollide and "below" in positionBetweeDoor:
                    pass
                else:
                    return
            self.walkDown()
        if key[pygame.K_d]:
            if (isWallCollide and "right" in positionBetweenWall):
                if isDoorCollide and "right" in positionBetweeDoor:
                    pass
                else:
                    return
            self.walkRight()

class Player2(Player):
    def __init__(self, *groups):
        super(Player2, self).__init__(20,20,*groups)
        for i in range(9):
            self.images[UP].append(pygame.image.load('pics/player1/up'+str(i)+'.png'))
            self.images[LEFT].append(pygame.image.load('pics/player1/left'+str(i)+'.png'))
            self.images[DOWN].append(pygame.image.load('pics/player1/down'+str(i)+'.png'))
            self.images[RIGHT].append(pygame.image.load('pics/player1/right'+str(i)+'.png'))
        self.image = self.images[DOWN][0]
        self.has_key = False

    def update(self,dt,game):
        key = pygame.key.get_pressed()
        
        isPlayerCollide = self.rect.colliderect(game.player1.rect)
        positionBetween = checkPostionBetweenRect(game.player1.rect,self.rect)

        isWallCollide = False
        positionBetweenWall = ""
        for wall in game.walls:
            if self.rect.colliderect(wall):
                isWallCollide = True
                positionBetweenWall += checkPostionBetweenRect(wall,self.rect)
                break

        isDoorCollide = False
        positionBetweeDoor = ""
        for door in game.doors:
            if self.rect.colliderect(door.rect):
                if (door.open):
                    isDoorCollide = True
                    positionBetweeDoor += checkPostionBetweenRect(door.rect,self.rect)
                    break
                
        if key[pygame.K_UP]:
            if (isWallCollide and "top" in positionBetweenWall):
                if isDoorCollide and "top" in positionBetweeDoor or "below" in positionBetweeDoor:
                    pass
                else:
                    return
            self.walkUp()
        if key[pygame.K_LEFT]:
            if (isWallCollide and "left" in positionBetweenWall):
                if isDoorCollide and "left" in positionBetweeDoor:
                    pass
                else:
                    return
            self.walkLeft()
        if key[pygame.K_DOWN]:
            if (isWallCollide and "below" in positionBetweenWall):
                if isDoorCollide and "below" in positionBetweeDoor:
                    pass
                else:
                    return
            self.walkDown()
        if key[pygame.K_RIGHT]:
            if (isWallCollide and "right" in positionBetweenWall):
                if isDoorCollide and "right" in positionBetweeDoor:
                    pass
                else:
                    return
            self.walkRight()
            
        if self.rect.colliderect(game.key) and not self.has_key:
            self.has_key = True
            game.sprites.remove(game.key)
            
    


    
    
