import pygame, sys
from pygame.locals import *
from player import *
from constant import *
from key import *
from alien import *
import random as r
from maze import *

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
        NUM_ROOMS = 7
        maze = Maze(NUM_GRID_ROWS, NUM_GRID_COLS, NUM_ROOMS)
        rooms, doors = maze.createMaze()
        rooms = sorted(rooms, key = lambda x: x.topLeft)
        rooms[0].hidden = False

        self.isPlaying = True
        while self.isPlaying:
            dt = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.sprites.update(dt/1000., self)           
            screen.fill(WHITE)
            self.sprites.draw(self.screen)
            self.drawMaze(rooms, doors)

            pygame.display.flip()

     
    def drawMaze(self, rooms, doors):
        tile_width = SCREEN_WIDTH*1.0/NUM_GRID_COLS
        tile_height = SCREEN_HEIGHT*1.0/NUM_GRID_ROWS

        for room in rooms:
            w = 0 if room.hidden else WALL_WIDTH
            x = room.topLeft[1]*tile_width
            y = room.topLeft[0]*tile_height
            pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, room.width*tile_width, room.height*tile_height), w)


        for door in doors:
           if door.room1.hidden and door.room2.hidden:
              continue
           colour = GREEN if door.open else RED
           x = door.col*tile_width
           y = door.row*tile_height
           offset = tile_height/4.0
           if door.vertical:
              pygame.draw.line(screen, colour, (x, y + offset), (x, y + tile_height - offset), DOOR_WIDTH)
           else:
              pygame.draw.line(screen, colour, (x + tile_width - offset, y), (x + offset, y), DOOR_WIDTH)
          

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("GUTS Hackathon")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    MainGame(screen).main()
