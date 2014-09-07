#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

class Tile:
   marked = False
   selected = False

   posX = 0
   posY = 0
   size = 0

   #color = GRAY
   color = (100, 100, 100)

   def __init__(self, posX, posY, size):
      self.posX = posX
      self.posY = posY
      self.size = size

   def draw(self, DISPLAYSURF):
      pygame.draw.rect(DISPLAYSURF, self.color,
                       (self.posX, self.posY, self.size, self.size))

   def setColor(self, color):
      self.color = color

   def getColor(self):
      return self.color

   def isMarked(self):
      return self.marked

   def isSelected(self):
      return self.selected
