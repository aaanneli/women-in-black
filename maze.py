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
      self.rect = pygame.Rect((self.topLeft[1]*TILE_WIDTH, self.topLeft[0]*TILE_HEIGHT), (self.width*TILE_WIDTH, self.height*TILE_HEIGHT))
      self.walls = []
     #top walls
      self.walls.append(pygame.Rect(self.topLeft[1] * TILE_WIDTH, self.topLeft[0] * TILE_HEIGHT, self.width * TILE_WIDTH, WALL_WIDTH))
      #bottom walls
      self.walls.append(pygame.Rect(self.topLeft[1] * TILE_WIDTH, self.bottomRight[0] * TILE_HEIGHT - WALL_WIDTH, self.width * TILE_WIDTH, WALL_WIDTH))
      #left walls
      self.walls.append(pygame.Rect(self.topLeft[1] * TILE_WIDTH, self.topLeft[0] * TILE_HEIGHT, WALL_WIDTH, self.height * TILE_HEIGHT))
      #Right Walls
      self.walls.append(pygame.Rect(self.bottomRight[1] * TILE_WIDTH - WALL_WIDTH, self.topLeft[0] * TILE_HEIGHT, WALL_WIDTH, self.height * TILE_HEIGHT))
           
   def containsPoint(self, row, col):
      return self.topLeft[0] <= row and self.topLeft[1] <= col and self.bottomRight[0] >= row and self.bottomRight[1] >= col

      
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
      door = Door(randint(room.topLeft[0], room.bottomRight[0]-1), column, True, None, None)
      return room1, room2, door


   def createHorizontalWall(self, room):
      row = randint(room.topLeft[0]+1, room.bottomRight[0]-1)
      room1 = Room(room.topLeft, (row, room.bottomRight[1]))
      room2 = Room((row, room.topLeft[1]), room.bottomRight)
      door = Door(row, randint(room.topLeft[1], room.bottomRight[1]-1), False, None, None)
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

      self.rooms = list(rooms.queue)
      for room in self.rooms:
         print room.topLeft, room.bottomRight
         
      for door in doors:
         print door.row, door.col
         self.findRooms(door)
         
      return self.rooms, doors

   
   def findRooms(self, door):
      drow = 0
      dcol = 0

      if door.vertical:
         drow = 1
         dcol = 0
      else:
         drow = 0
         dcol = 1
      
         
      for room in self.rooms:
         if room.containsPoint(door.row, door.col) and room.containsPoint(door.row + drow, door.col + dcol):
            if door.room1 == None:
               door.room1 = room
            else:
               door.room2 = room
               break
            
      print door.room1.topLeft, door.room2.topLeft




