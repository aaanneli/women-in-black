# Class to produce random map layouts
from random import *
from Queue import *
from constant import *
import pygame


class Door:
   def __init__(self, row, col, vertical, room1, room2):
      self.row = row
      self.col = col
      self.open = False
      self.vertical = vertical
      self.room1 = room1
      self.room2 = room2
      x = col * TILE_WIDTH
      y = row * TILE_HEIGHT
      if vertical:
         realX = x - 0.25
         realY = y + DOOR_OFFSET
         realWidth = DOOR_WIDTH
         realHeight = TILE_HEIGHT / 2.0
      else:
         realX = x + DOOR_OFFSET
         realY = y - 0.25
         realWidth = TILE_WIDTH / 2.0
         realHeight = DOOR_WIDTH
      self.rect = pygame.Rect(realX, realY,realWidth,realHeight)


   def openDoor(self):
      self.open = True

   def close(self):
      self.open = False



class Room:
   def __init__(self, topLeft, bottomRight):
      self.topLeft = topLeft
      self.bottomRight = bottomRight
      self.hidden = True
      self.width = bottomRight[1] - topLeft[1] 
      self.height = bottomRight[0] - topLeft[0]
      self.rect = pygame.Rect(self.topLeft,(self.width,self.height))
      self.walls = []
      #top walls
      self.walls.append(pygame.Rect(self.topLeft[1] * TILE_WIDTH, self.topLeft[0] * TILE_HEIGHT ,self.width * TILE_WIDTH, WALL_WIDTH))
      #bottom walls
      self.walls.append(pygame.Rect(self.topLeft[1] * TILE_WIDTH, (self.topLeft[0] + self.height) * TILE_WIDTH - WALL_WIDTH, self.width * TILE_HEIGHT ,WALL_WIDTH))
      #left walls
      self.walls.append(pygame.Rect(self.topLeft[1] * TILE_WIDTH, self.topLeft[0] * TILE_HEIGHT, WALL_WIDTH, self.height * TILE_WIDTH))
      #Right Walls
      self.walls.append(pygame.Rect((self.topLeft[1] + self.width) * TILE_WIDTH - WALL_WIDTH, self.topLeft[0] * TILE_HEIGHT, WALL_WIDTH, self.height * WALL_WIDTH))

      
   def unhide(self):
      self.hidden = False
      
      
 
class Maze:
   def __init__(self, rows, cols, numRooms):
       self.rooms = []
       self.rows = rows
       self.cols = cols
       self.numRooms = numRooms


   def createVerticalWall(self, room):
      column = randint(room.topLeft[1]+1, room.bottomRight[1]-1)
      room1 = Room(room.topLeft, (room.bottomRight[0], column))
      room2 = Room((room.topLeft[0], column), room.bottomRight)
      door = Door(randint(room.topLeft[0], room.bottomRight[0]-1), column, True, room1, room2)
      return room1, room2, door


   def createHorizontalWall(self, room):
      row = randint(room.topLeft[0]+1, room.bottomRight[0]-1)
      room1 = Room(room.topLeft, (row, room.bottomRight[1]))
      room2 = Room((row, room.topLeft[1]), room.bottomRight)
      door = Door(row, randint(room.topLeft[1], room.bottomRight[1]-1), False, room1, room2)
      return room1, room2, door
   
 
   def createMaze(self):
      rooms = Queue()
      rooms.put(Room((0, 0), (self.rows, self.cols)))
      doors = []

      i = 0;
      
      while rooms.qsize() != self.numRooms and i < 1000:
         room = rooms.get()
         
         if room.width > room.height:
            if room.width <= 3:
               rooms.put(room)
            else:
               room1, room2, door = self.createVerticalWall(room)
               rooms.put(room1)
               rooms.put(room2)
               doors += [door]
         else:
            if room.height <= 3:
               rooms.put(room)
            else:
               room1, room2, door = self.createHorizontalWall(room)
               rooms.put(room1)
               rooms.put(room2)
               doors += [door]
               
            i += 1

      return list(rooms.queue), doors





