#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, random
from pygame.locals import *

pygame.init()

## Capturar dimensões da tela em fullscreen
HEIGHT = 1000
WIDTH  = 1000

# Cria a janela
DISPLAYSURF = pygame.display.set_mode((HEIGHT, WIDTH), 0, 32)
pygame.display.set_caption('Memory Matrix')

# Define as cores
BLACK = (  0,   0,   0)
GRAY  = (100, 100, 100)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# Preenche o surface com a cor especificada
DISPLAYSURF.fill(WHITE)

# Define o tamanho do cabeçalho e o padding da janela e a borda da matriz
HEADER = 100
PADDING = min(HEIGHT-HEADER, WIDTH) * 0.03

# Define as dimensões úteis para o desenho da matriz
BODY_HEIGHT = HEIGHT - HEADER - 2*PADDING
BODY_WIDTH = WIDTH - 2*PADDING

# Define o espaço entre os tiles em função do tamanho do tile
## Usar também o número de tiles para essa decisão
## Caso contrário quando houver poucos tiles a borda irá ficar fina ou quando houver muitos a borda irá ficar grossa
TILE_INTERSPACE_FACTOR = 0.1

## Calcular nível
level = 3
## A partir do nível definir o número de tiles (e.g. 3x4)
numTilesLower = 2     # Este deve ser sempre o menor lado
numTilesGreater = 3   # Este deve ser sempre o maior lado

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
# Desenha o board
pygame.draw.rect(DISPLAYSURF, BLACK, (marginLeft, marginUpper, boardSizeWidth, boardSizeHeight))

# Desenha os tiles
for i in range(0, numTilesWidth):
   posX = i*(tileSize+tileInterspace) + border + marginLeft
   for j in range(0, numTilesHeight):
      posY = j*(tileSize+tileInterspace) + border + marginUpper
      pygame.draw.rect(DISPLAYSURF, GRAY, (posX, posY, tileSize, tileSize))

# Executa o game loop
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
   pygame.display.update()
