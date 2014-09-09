#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

import pygame
from pygame.locals import *

from Tile import *
from Colors import *
from MemoryMatrixConf import *

class Board:

   #### setDimensions ####

   # Número de tiles (X e Y)
   numTilesWidth = 3
   numTilesHeight = 3
   # Tamanho do tile
   tileSize = 100
   # Espaço entre os tiles
   tileInterspace = 10
   # Tamanho da borda
   border = 20
   # Tamanho do board (X e Y)
   sizeWidth = 360
   sizeHeight = 360

   #### setPosition ####

   # Posição onde será desenhado
   posX = 0
   posY = 0

   # Matriz com as instâncias de Tiles
   matrix = []

   # Cor do board
   color = BLACK

   def __init__(self, numTiles, tileSize, color):
      """Define a cor e as dimensões do board, bem como a de seus tiles"""
      # Define a cor do board
      self.setColor(color)
      # Calcula as dimensões do board
      self.setDimensions(numTiles, tileSize)
      
      # Instancia os tiles da matrix
      for i in range(0, self.numTilesHeight):
         # Cria cada linha da matrix
         row = []
         # Define a posição Y (especifica a linha)
         posY = i*(self.tileSize+self.tileInterspace) + self.border + self.posY

         for j in range(0, self.numTilesWidth):
            # Define a posição X (especifica a coluna)
            posX = j*(self.tileSize+self.tileInterspace) + self.border + self.posX
            # Cria as dimensões do tile
            rect = pygame.Rect(posX, posY, self.tileSize, self.tileSize)
            # Instancia e concatena os Tiles para a lista row
            row = row + [Tile(rect, COLOR_TILE)]

         # Concatena as linhas para a lista matrix
         self.matrix = self.matrix + [row]

   def setColor(self, color):
      """Define a cor do board"""
      self.color = color

   def setDimensions(self, numTiles, tileSize):
      """Define as dimensões do board,
         número de tiles, tamanho do tile,
         espaço entre tiles, tamanho da borda
      """
      # Número de tiles (Y e X) e tamanho dos tiles
      self.numTilesHeight, self.numTilesWidth = numTiles
      self.tileSize = tileSize

      # Calcula o tamanho do tileInterspace
      self.tileInterspace = self.tileSize*TILE_INTERSPACE_FACTOR
      # Calcula o tamanho do border
      self.border = TILE_BORDER_FACTOR * self.tileInterspace

      # Define o tamanho do board onde será desenhada a matriz
      self.sizeHeight = self.tileSize * self.numTilesHeight + \
                        self.tileInterspace * (self.numTilesHeight-1) + \
                        2 * self.border
      self.sizeWidth = self.tileSize * self.numTilesWidth + \
                       self.tileInterspace * (self.numTilesWidth-1) + \
                       2 * self.border

   def setPositionCentral(self, windowSize, offset):
      """Usada para definir a posição da matriz que por padrão é 0,0
         Essa função irá receber as dimensões da janela e o offset
         para centralizar a matriz na janela
      """
      # Variáveis locais para conter altura e largura da janela
      height, width = windowSize
      # Variáveis locais para conter o offset da altura e largura
      offsetY, offsetX = offset

      # Define a margem superior e a esquerda para desenhar o board
      marginUpper = (height+offsetY - self.sizeHeight) / 2
      marginLeft  = (width+offsetX - self.sizeWidth) / 2
      self.setPosition((marginUpper, marginLeft))

   def setPosition(self, position):
      """Define a posição da matriz de acordo com os valores X e Y"""
      self.posY, self.posX = position

      # Após qualquer alteração da posição da matriz
      # seus tiles também devem ser atualizados
      self.updateTilesPosition()

   def updateTilesPosition(self):
      """Atualiza a posição dos tiles baseado na posição do board"""
      for i in range(0, self.numTilesHeight):
         # Define a posição Y (especifica a linha)
         posY = i*(self.tileSize+self.tileInterspace) + self.border + self.posY

         for j in range(0, self.numTilesWidth):
            # Define a posição X (especifica a coluna)
            posX = j*(self.tileSize+self.tileInterspace) + self.border + self.posX
            self.matrix[i][j].setPosition((posY, posX))

   def setMarkedTiles(self, numMarkedTiles):
      """Escolhe quais tiles irão ser marcados"""
      ## Levar em consideração chuncks e as repetições
      for i in range(numMarkedTiles):
         self.matrix[random.randint(0, self.numTilesHeight-1)] \
                    [random.randint(0, self.numTilesWidth-1)].marked = True

   def showMarkedTiles(self, DISPLAYSURF):
      """Exibe na tela os tiles marcados"""
      for i in range(0, self.numTilesWidth):
         for j in range(0, self.numTilesHeight):
            # Verifica se o tile está marcado
            if self.matrix[j][i].isMarked():
               # Se sim, troca sua cor e o desenha
               self.matrix[j][i].setColor(COLOR_MARKED_TILE)
               self.matrix[j][i].draw(DISPLAYSURF)
      
   def hideMarkedTiles(self, DISPLAYSURF):
      """Oculta da tela os tiles marcados"""
      for i in range(0, self.numTilesWidth):
         for j in range(0, self.numTilesHeight):
            # Verifica se o tile está marcado
            if self.matrix[j][i].isMarked():
               # Se sim, troca sua cor e o desenha
               self.matrix[j][i].setColor(COLOR_TILE)
               self.matrix[j][i].draw(DISPLAYSURF)

   def draw(self, DISPLAYSURF):
      """Desenha tanto o board quanto os tiles na tela"""
      # Desenha o board
      pygame.draw.rect(DISPLAYSURF, self.color, \
                       (self.posX, self.posY, self.sizeWidth, self.sizeHeight))

      # Desenha os tiles
      for i in range(0, self.numTilesWidth):
         for j in range(0, self.numTilesHeight):
            self.matrix[j][i].draw(DISPLAYSURF)

      ## Daqui pra baixo deve ser apagado
      pygame.display.update()
      time.sleep(.5)

      self.showMarkedTiles(DISPLAYSURF)

      pygame.display.update()
      time.sleep(3)

      self.hideMarkedTiles(DISPLAYSURF)
