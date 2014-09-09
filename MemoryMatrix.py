#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import pygame
from pygame.locals import *

from Tile import *
from Board import *
from Colors import *
from MemoryMatrixConf import *

pygame.init()

## Capturar dimensões da tela em fullscreen
HEIGHT = 1000
WIDTH  = 600

# Cria a janela
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Memory Matrix')

# Preenche o surface com a cor especificada
DISPLAYSURF.fill(COLOR_WINDOW)

# Define o tamanho do padding
PADDING = min(HEIGHT-HEADER, WIDTH) * 0.03

# Define as dimensões úteis para o desenho da matriz
BODY_HEIGHT = HEIGHT - HEADER - 2*PADDING
BODY_WIDTH = WIDTH - 2*PADDING

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
# Como número de tiles pode variar no eixo X e Y, deve-se fazer os dois cálculos e usar o menor
# Isso é demonstrado nos testes de mesa 1 e 2
tileSize = min(tileSizeH, tileSizeW)

# Com o maior tamanho possível para o tile definido, pode-se criar o board
board = Board((numTilesHeight, numTilesWidth), tileSize, COLOR_BOARD)
# Depois de criado ele deve ser centralizado na tela
board.setPositionCentral((HEIGHT, WIDTH), (HEADER, 0))
# E enfim alguns tiles devem ser marcados de acordo com o nível
board.setMarkedTiles(level)

# DESENHAR

# Desenha o board
board.draw(DISPLAYSURF)

# Executa o game loop
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
   pygame.display.update()
