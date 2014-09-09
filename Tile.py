#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from Colors import *

class Tile:
   # Define se o tile foi marcado
   marked = False
   # Define se o usuário selecionou o tile
   selected = False

   # Armazena o tamanho e a posição do tile
   rect = pygame.Rect(0, 0, 0, 0)

   # Armazena a cor do tile
   color = DIMGRAY

   def __init__(self, rect, color):
      """Define a cor e as dimensões do tile"""
      self.rect = rect
      self.setColor(color)

   def setPosition(self, position):
      """Define as dimensões do tile"""
      posX, posY = position
      self.rect = (posX, posY, self.rect.width, self.rect.height)

   def setColor(self, color):
      """Define a cor do tile"""
      self.color = color

   def isMarked(self):
      """Verifica se o tile está marcado"""
      return self.marked

   def isSelected(self):
      """Verifica se o tile foi selecionado"""
      return self.selected

   def draw(self, DISPLAYSURF):
      """Desenha o tile na tela"""
      pygame.draw.rect(DISPLAYSURF, self.color, self.rect)

