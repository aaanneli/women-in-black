from __future__ import print_function, division
 
import pygame
import random
import math
from constant import *


def radians_to_degrees(radians):
    return (radians / math.pi) * 180.0

class Bullet(pygame.sprite.Sprite):
    side = 7 # small side of bullet rectangle
    vel = 250 # velocity
    maxlifetime = 10.0 # seconds

    def __init__(self, boss, *groups ):
        pygame.sprite.Sprite.__init__(self, *groups) # THE most important line !
        self.boss = boss
        self.lifetime = 0.0
        self.calculate_heading() # !!!!!!!!!!!!!!!!!!!
        self.pos = self.boss.pos[:] # copy (!!!) of boss position 
        #self.pos = self.boss.pos   # uncomment this linefor fun effect
        self.calculate_origin()
        self.update() # to avoid ghost sprite in upper left corner, 
                      # force position calculation.
 
    def calculate_heading(self):
        """ drawing the bullet and rotating it according to it's launcher"""
        self.radius = Bullet.side # for collision detection
        self.angle = -math.degrees(self.boss.angle)
        image = pygame.Surface((Bullet.side * 2, Bullet.side)) # rect 2 x 1
        image.fill((128,128,128)) # fill grey
        pygame.draw.rect(image, BLACK, (0,0,int(Bullet.side * 1.5), Bullet.side)) # rectangle 1.5 length
        pygame.draw.circle(image, BLACK, (int(self.side *1.5) ,self.side//2), self.side//2) #  circle
        image.set_colorkey((128,128,128)) # grey transparent
        self.image0 = image.convert_alpha()
        self.image = pygame.transform.rotate(self.image0, self.angle)
        self.rect = self.image.get_rect()
        self.dx = math.cos(self.boss.angle) * self.vel
        self.dy = math.sin(self.boss.angle) * self.vel
        if self.boss.isMoving:
            # add boss movement
            self.dx += math.cos(self.boss.angle) * MOVING_INDEX*FPS
            self.dy += math.sin(self.boss.angle) * MOVING_INDEX*FPS 
        
        
    def calculate_origin(self):
        # - spawn bullet at end of turret barrel instead tank center -
        # cannon is around Tank.side long, calculatet from Tank center
        # later subtracted 20 pixel from this distance
        # so that bullet spawns closer to tank muzzle
        #self.pos[0] +=  math.cos(degrees_to_radians(self.boss.turretAngle)) #* (Tank.side-20)
        #self.pos[1] +=  math.sin(degrees_to_radians(-self.boss.turretAngle))#* (Tank.side-20)
        self.pos[0] = self.boss.rect.center[0]
        self.pos[1] = self.boss.rect.center[1]

 
    def update(self, seconds=0.0,game = None):
        # ---- kill if too old ---
        self.lifetime += seconds
        if self.lifetime > Bullet.maxlifetime:
            self.kill()
        # ------ calculate movement --------
        self.pos[0] += self.dx * seconds
        self.pos[1] += self.dy * seconds

        # ----- kill if out of screen
        if self.pos[0] < 0:
            self.kill()
        elif self.pos[0] > SCREEN_WIDTH:
            self.kill()
        if self.pos[1] < 0:
            self.kill()
        elif self.pos[1] > SCREEN_HEIGHT:
            self.kill()
        #------- move -------
        self.rect.centerx = round(self.pos[0],0)
        self.rect.centery = round(self.pos[1],0)
