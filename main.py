import pygame, sys
from pygame.locals import *
from player import *
from constant import *
from key import *
from alien import *
import random as r
from maze import *
from boss import *



class MainGame():
    def __init__(self,screen):

        self.screen = screen
        self.isMenu = True
        self.isPlaying = True
        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        self.player1 = Katya(self.sprites)
        self.player2 = Player2(self.sprites)
        self.keys = [] #Key(self.sprites)
        self.isWin = False
        self.isWinning = False
        self.portal = None
        self.rooms = []
        self.walls = []
        self.doors = []
        self.aliens = []
        self.roomCenter = []
        self.boss = None
        self.bg = pygame.image.load("pics/background.png")
        self.menuBG = pygame.image.load("start_files/bg.png")
        self.duoPic = pygame.image.load("start_files/duo.png")
        self.instructionPic = pygame.image.load("start_files/instructions.png")

    def main(self):
        maze = Maze(NUM_GRID_ROWS, NUM_GRID_COLS)
        rooms, doors = maze.createMaze()
        rooms = sorted(rooms, key = lambda x: x.topLeft)
        self.rooms = rooms

        NUM_ROOMS = len(rooms)
        self.startRoom = rooms[0];
        endRoomIndex = randint(0, NUM_ROOMS-1);

        self.endRoom = rooms[endRoomIndex]
        
        for room in rooms:
            self.walls += room.walls
            self.keys += [Key(room, self.sprites)]
            self.roomCenter.append(room.rect.center)
        for door in doors:
            self.doors.append(door)

            
        self.startRoom.hidden = False
        
        self.generateAlien(NUMBER_OF_ALIENS)        

        while self.isMenu:
            self.screen.blit(self.menuBG, (0, 0))
            self.screen.blit(self.instructionPic, (SCREEN_WIDTH // 2 - 215, 150))
            self.screen.blit(self.duoPic, (SCREEN_WIDTH // 2 - 33 , 425))
            titleFont = pygame.font.Font('start_files/LLPIXEL3.ttf', 75)
            textSurf,TextRect = text_objects("Women in Black", titleFont)
            TextRect.center = ((SCREEN_WIDTH//2),(50))
            textSurf = titleFont.render('Women In Black', True,WHITE)
            self.screen.blit(textSurf, TextRect)
            titleFont2 = pygame.font.Font('start_files/LLPIXEL3.ttf', 32)
            textSurf2,TextRect2 = text_objects("Press SPACE to Continue", titleFont2)
            TextRect2.center = ((SCREEN_WIDTH//2),(525))
            textSurf2 = titleFont2.render('Press SPACE to Continue', True,WHITE)
            self.screen.blit(textSurf2, TextRect2)


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.isMenu = False
                pygame.time.wait(300)
            pygame.display.flip()
            
        pygame.mixer.music.load("music/arcade-music.wav")
        pygame.mixer.music.play(-1)
        
        self.isPlaying = True
        while self.isPlaying:
            self.screen.blit(self.bg, (0, 0))
            dt = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.sprites.update(dt/1000., self)           
            self.sprites.draw(self.screen)
            self.drawMaze(rooms, doors)
            
            if self.isWinning :
                self.portal = pygame.Rect(self.endRoom.rect.center[0] - TILE_WIDTH/4.0, self.endRoom.rect.center[1] - TILE_HEIGHT/4.0, TILE_WIDTH/2.0, TILE_HEIGHT/2.0)
                pygame.draw.rect(self.screen, BLUE, self.portal)
            if len(self.aliens) < NUMBER_OF_ALIENS * 0.25:
                self.generateAlien(3)
            pygame.display.flip()

        pygame.mixer.music.stop()
        endScene = True
        endText = ""
        if self.isWin:
            endText = "YOU WIN!"
            color = GREEN
            winSound = pygame.mixer.Sound("music/victory.wav")
            winSound.play()
        else:
            endText = "YOU LOSE!"
            color = RED
            loseSound = pygame.mixer.Sound("music/evil-laugh.wav")
            gameOverSound = pygame.mixer.Sound("music/game-over.wav")
            loseSound.play()
            gameOverSound.play()
            
        myfont = pygame.font.SysFont('Comic Sans MS', 72)
        endTextSurface = myfont.render(endText,False,BLACK)
        while endScene:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                endScene = False
            
            screen.fill(color)
            self.screen.blit(endTextSurface,(SCREEN_WIDTH * 0.33 , SCREEN_HEIGHT * 0.33))
            pygame.display.flip()
            
        pygame.quit()
        sys.exit()

    def areWeWinning(self):
        for door in self.doors:
            if not door.open:
                return False
        self.isWinning = True
        self.boss = Boss(self.endRoom.rect.center[0] - TILE_WIDTH/4.0, self.endRoom.rect.center[1] - TILE_HEIGHT/4.0,self.sprites)
        return True
            

     
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

    def generateAlien(self, numOfAliens):
        for i in range(numOfAliens):
            size = 0
            while (size < NUM_GRID_ROWS * NUM_GRID_COLS * 0.10):
                index = r.randint(1,NUM_ROOMS - 1)
                size = self.rooms[index].getSize()
            self.aliens.append(Alien(r.randint(self.roomCenter[index][0] - self.rooms[index].getWidth() // 4, self.roomCenter[index][0] + self.rooms[index].getWidth() // 4),
                                     r.randint(self.roomCenter[index][1] - self.rooms[index].getHeight() // 4, self.roomCenter[index][1] + self.rooms[index].getHeight() // 4),
                                     self.sprites))

    
                                     
          

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Woman in Black")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    MainGame(screen).main()
