#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from Colors import *

class Tile:
   marked = False
   selected = False

   rect = pygame.Rect(0, 0, 0, 0)

   color = DIMGRAY

   def __init__(self, rect, color):
      self.rect = rect
      self.setColor(color)

   def draw(self, DISPLAYSURF):
      pygame.draw.rect(DISPLAYSURF, self.color, self.rect)

   def setColor(self, color):
      self.color = color

   def getColor(self):
      return self.color

   def isMarked(self):
      return self.marked

   def isSelected(self):
      return self.selected
