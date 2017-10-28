import pygame, sys
from pygame.locals import *
from player import *
from constant import *
from key import *
from alien import *
import random as r

class MainGame():
    def __init__(self,screen):
        self.screen = screen
        self.isPlaying = True
        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        self.player1 = Player1(self.sprites)
        self.player2 = Player2(self.sprites)
        self.key = Key(self.sprites)
        self.aliens = []
        for i in range(1):
            self.aliens.append(Alien(r.randint(0,SCREEN_WIDTH),\
                                     r.randint(0,SCREEN_HEIGHT),self.sprites))
        

    def main(self):
        self.isPlaying = True
        while self.isPlaying:
            dt = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.sprites.update(dt/1000., self)           
            screen.fill(BLACK)
            self.sprites.draw(self.screen)
            pygame.display.flip()
     


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("GUTS Hackathon")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    MainGame(screen).main()
