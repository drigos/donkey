#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random
import time

import numpy as np
import pygame
from pygame.locals import *

from Tile import *
from Colors import *

pygame.init()

# Capturar dimensões da tela em fullscreen
HEIGHT = 1000
WIDTH  = 600

# Define cores
COLOR_WINDOW = WHITE
COLOR_BOARD = BLACK
COLOR_TILE = DIMGRAY
COLOR_MARKED_TILE = CYAN
COLOR_HOVER_TILE = GRAY
COLOR_SELECTED_TILE = DARKSLATEGRAY

# Cria a janela
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Memory Matrix')

# Preenche o surface com a cor especificada
DISPLAYSURF.fill(COLOR_WINDOW)

# Define o tamanho do cabeçalho e o padding da janela e a borda da matriz
HEADER = 100
PADDING = min(HEIGHT-HEADER, WIDTH) * 0.03

# Define as dimensões úteis para o desenho da matriz
BODY_HEIGHT = HEIGHT - HEADER - 2*PADDING
BODY_WIDTH = WIDTH - 2*PADDING

# Define o espaço entre os tiles em função do tamanho do tile
TILE_INTERSPACE_FACTOR = 0.1

## Calcular nível
level = 17
## A partir do nível definir o número de tiles (e.g. 3x4)
numTilesLower = 6     # Este deve ser sempre o menor lado
numTilesGreater = 7   # Este deve ser sempre o maior lado

# Se a divisão da largura da tela pela altura retornar um número maior que um
# então a tela tem orientação horizontal, caso contrário orientação vertical
if (BODY_WIDTH / BODY_HEIGHT > 1): # Orientação horizontal
   # Nesse caso a maior dimensão (núm. tiles) da matriz ficará na largura
   numTilesHeight = numTilesLower
   numTilesWidth = numTilesGreater
else:                               # Orientação vertical
   # Nesse caso a maior dimensão (núm. tiles) da matriz ficará na altura
   numTilesHeight = numTilesGreater
   numTilesWidth = numTilesLower

# A fórmula usada aqui é uma fatoração da seguinte fórmula
# BODY_HEIGHT == numTiles*tileSize + (numTiles - 1)*tileInterspace + 2*border
# Onde border está em função do tileInterspace (border == 2*tileInterspace)
# Onde o tileInterspace está em função do tamanho do tile
# BODY_HEIGHT == numTiles*tileSize + (numTiles - 1)*(tileSize*TILE_INTERSPACE_FACTOR) + 4*(tileSize*TILE_INTERSPACE_FACTOR)
tileSizeH = BODY_HEIGHT / (numTilesHeight + TILE_INTERSPACE_FACTOR*(numTilesHeight + 3))
tileSizeW = BODY_WIDTH / (numTilesWidth + TILE_INTERSPACE_FACTOR*(numTilesWidth + 3))
# Como número de tiles pode variar no eixo X e Y, deve-se fazer os dois cálculo e usar o menor
# Isso é demonstrado nos testes de mesa 1 e 2
tileSize = min(tileSizeH, tileSizeW)

# Aqui é dado um valor em pixel para o tileInterspace
tileInterspace = tileSize*TILE_INTERSPACE_FACTOR
# Aqui é dado um valor em pixels para o border
border = 2 * tileInterspace

# Define o tamanho do board onde será desenhada a matriz
boardSizeHeight = tileSize*numTilesHeight + tileInterspace*(numTilesHeight-1) + 2*border
boardSizeWidth = tileSize*numTilesWidth + tileInterspace*(numTilesWidth-1) + 2*border
# Define a margem esquerda e superior para desenhar o board
marginUpper = (HEIGHT+HEADER - boardSizeHeight) / 2
marginLeft = (WIDTH - boardSizeWidth) / 2

# Cria a matriz que irá receber os Tiles
matrix = []

# Instancio os tiles da matrix
for i in range(0, numTilesHeight):
   # Cria cada linha da matrix
   row = []
   # Define a posição Y (especifica a linha)
   posY = i*(tileSize+tileInterspace) + border + marginUpper

   for j in range(0, numTilesWidth):
      # Define a posição X (especifica a coluna)
      posX = j*(tileSize+tileInterspace) + border + marginLeft
      # Cria as dimensões do tile
      rect = pygame.Rect(posX, posY, tileSize, tileSize)
      # Instancia e concatena os Tiles para a lista row
      row = row + [Tile(rect, COLOR_TILE)]

   # Concatena as linhas para a lista matrix
   matrix = matrix + [row]

# Escolhe quais tiles irão ser marcados
## Levar em consideração chuncks e as repetições
for i in range(level):
   matrix[random.randint(0, numTilesHeight-1)][random.randint(0, numTilesWidth-1)].marked = True

# DESENHAR

# Desenha o board
pygame.draw.rect(DISPLAYSURF, COLOR_BOARD, (marginLeft, marginUpper, boardSizeWidth, boardSizeHeight))

# Desenha os tiles
for i in range(0, numTilesWidth):
   for j in range(0, numTilesHeight):
      matrix[j][i].draw(DISPLAYSURF)

pygame.display.update()
time.sleep(.5)

# Desenha os tiles marcados
for i in range(0, numTilesWidth):
   for j in range(0, numTilesHeight):
      if matrix[j][i].isMarked():
         matrix[j][i].setColor(COLOR_MARKED_TILE)
         matrix[j][i].draw(DISPLAYSURF)

pygame.display.update()
time.sleep(3)

# Apaga os tiles marcados
for i in range(0, numTilesWidth):
   for j in range(0, numTilesHeight):
      if matrix[j][i].isMarked():
         matrix[j][i].setColor(COLOR_TILE)
         matrix[j][i].draw(DISPLAYSURF)

# Executa o game loop
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
   pygame.display.update()
