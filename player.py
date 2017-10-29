import pygame, sys
from pygame.locals import *
from constant import *
from key import *
from maze import *
from bullet import *
from math import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super(Player, self).__init__(*groups)
        self.images = [[] for i in range(4)]
        self.index = 0
        self.direction = RIGHT
        self.x = x
        self.y = y
        self.width = CHARACTER_WIDTH
        self.height = CHARACTER_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.isMoving = False
        self.has_key = False

    def update(self,dt,game):
        pass

    def walkUp(self,game):
        self.direction = UP
        self.rect.y -= MOVING_INDEX
        if self.ableToWalkThroughDoor(game):
            pass
        elif self.hitWall(game.walls):
            self.rect.y += MOVING_INDEX
        self.image = self.images[UP][self.index]
        self.index = (self.index + 1) % len(self.images[UP])

    def walkDown(self,game):
        self.direction = DOWN
        self.rect.y += MOVING_INDEX
        if self.ableToWalkThroughDoor(game):
            pass
        elif self.hitWall(game.walls):
            self.rect.y -= MOVING_INDEX
        self.image = self.images[DOWN][self.index]
        self.index = (self.index + 1) % len(self.images[DOWN])


    def walkRight(self,game):
        self.direction = RIGHT
        self.rect.x += MOVING_INDEX
        if self.ableToWalkThroughDoor(game):
            pass
        elif self.hitWall(game.walls):
            self.rect.x -= MOVING_INDEX
        self.image = self.images[RIGHT][self.index]
        self.index = (self.index + 1) % len(self.images[RIGHT])

    def walkLeft(self,game):
        self.direction = LEFT
        self.rect.x -= MOVING_INDEX
        if self.ableToWalkThroughDoor(game):
            pass
        elif self.hitWall(game.walls):
            self.rect.x += MOVING_INDEX
        self.image = self.images[LEFT][self.index]
        self.index = (self.index + 1) % len(self.images[LEFT])

    def useAbility(self):
        pass

    def hitWall(self,wallList):
        for wall in wallList:
            if self.rect.colliderect(wall):
                return True
        return False

    def ableToWalkThroughDoor(self,game):
        for door in game.doors:
            if self.rect.colliderect(door.rect):
                if door.open:
                    return True
                elif not door.open and self.has_key:
                    door.open = True
                    door.room1.hidden = False
                    door.room2.hidden = False
                    self.has_key = False
                    game.areWeWinning()
                    return True
        return False
                


class Katya(Player):
    firekey = (pygame.K_SPACE)
    
    recoiltime = 0.75

    def __init__(self, *groups):

        super(Katya, self).__init__(10,10,*groups)

        self.pos = [self.x,self.y]
        self.angle = 0
        
        for i in range(3):
            self.images[UP].append(pygame.image.load('pics/character_2/up'+str(i)+'.png'))
            self.images[LEFT].append(pygame.image.load('pics/character_2/left'+str(i)+'.png'))
            self.images[DOWN].append(pygame.image.load('pics/character_2/down'+str(i)+'.png'))
            self.images[RIGHT].append(pygame.image.load('pics/character_2/right'+str(i)+'.png'))
        self.image = self.images[DOWN][0]

        self.firekey = Katya.firekey
        self.firestatus = 0.0

    def update(self,dt,game):
        key = pygame.key.get_pressed()    

        isDoorCollide = False
        positionBetweeDoor = ""
        for door in game.doors:
            if self.rect.colliderect(door.rect):
                if (door.open):
                    isDoorCollide = True
                    positionBetweeDoor += checkPostionBetweenRect(door.rect,self.rect)

      
        if key[pygame.K_w]:
            self.isMoving = True
            self.walkUp(game)
            self.angle = math.pi * 3 / 2
        if key[pygame.K_a]:
            
            self.isMoving = True

            self.walkLeft(game)
            self.angle = math.pi

        if key[pygame.K_s]:
            
            self.isMoving = True
            self.walkDown(game)
            self.angle = math.pi / 2
        if key[pygame.K_d]:

           

            self.isMoving = True
            self.walkRight(game)
            self.angle = 0

        if (self.firestatus == 0.0):
            
            if key[self.firekey]:
                shootSound = pygame.mixer.Sound("music/shoot.wav")
                shootSound.play()
                
                self.firestatus = Katya.recoiltime # seconds until Katya can fire again
                Bullet(self,game.sprites)
        self.firestatus -= 0.1
        if self.firestatus < 0.0:
            self.firestatus = 0

        self.isMoving = False
        

class Player2(Player):
    def __init__(self, *groups):
        super(Player2, self).__init__(20,20,*groups)
        for i in range(3):
            self.images[UP].append(pygame.image.load('pics/character_1/up'+str(i)+'.png'))
            self.images[LEFT].append(pygame.image.load('pics/character_1/left'+str(i)+'.png'))
            self.images[DOWN].append(pygame.image.load('pics/character_1/down'+str(i)+'.png'))
            self.images[RIGHT].append(pygame.image.load('pics/character_1/right'+str(i)+'.png'))
        self.image = self.images[DOWN][0]
        self.has_key = False

    def update(self,dt,game):
        key = pygame.key.get_pressed()

        isDoorCollide = False
        positionBetweeDoor = ""
        for door in game.doors:
            if self.rect.colliderect(door.rect):
                if not door.open:
                    if self.has_key:
                        openDoorSound = pygame.mixer.Sound("music/portal-open.wav")
                        openDoorSound.play()
                        
                        door.openDoor()
                        self.has_key = False
                        door.room1.hidden = False
                        door.room2.hidden = False
                        game.areWeWinning()
                elif (door.open):
                    isDoorCollide = True
                    positionBetweeDoor += checkPostionBetweenRect(door.rect,self.rect)

        if key[pygame.K_UP]:
            self.walkUp(game)
        if key[pygame.K_LEFT]:
            self.walkLeft(game)
        if key[pygame.K_DOWN]:
            self.walkDown(game)
        if key[pygame.K_RIGHT]:
            self.walkRight(game)

        if (game.portal is not None):
            if self.rect.colliderect(game.portal):
                if game.isWinning and self.has_key and game.boss is None:
                    game.isWin = True
                    game.isPlaying = False

        for actualkey in game.keys:
            if self.rect.colliderect(actualkey.rect) and not self.has_key:
                keyPickupSound = pygame.mixer.Sound("music/key-pickup.wav")
                keyPickupSound.play()
                
                self.has_key = True
                game.keys.remove(actualkey)
                game.sprites.remove(actualkey)
                
        if self.has_key:
                pygame.draw.rect(game.screen, YELLOW, pygame.Rect(self.rect.x, self.rect.y - 10, self.width, 10))
                        


        

    
    
