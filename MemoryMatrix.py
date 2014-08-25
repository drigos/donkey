#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, random
from pygame.locals import *

pygame.init()

# Cria a janela
DISPLAYSURF = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption('Memory Matrix')

# Define as cores
BLACK = (  0,   0,   0)
GRAY  = (100, 100, 100)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

TILE_SIZE = 48
TILE_INTERSPACE = 4
BOARD_BORDER = 8
MIN_TILES = 3
MAX_TILES = 18

WINDOW_BORDER = 26

# Preenche o surface com a cor especificada
DISPLAYSURF.fill(WHITE)

# Gera um número aleatório para ser o número de tiles e desenha o board
tilesAmount = random.randint(MIN_TILES, MAX_TILES)
boardSize = TILE_SIZE*tilesAmount + TILE_INTERSPACE*(tilesAmount-1) + 2*BOARD_BORDER
pygame.draw.rect(DISPLAYSURF, BLACK, (WINDOW_BORDER, WINDOW_BORDER, boardSize, boardSize))

# Desenha os tiles
for i in range(0, tilesAmount):
   posX = i*(TILE_SIZE+TILE_INTERSPACE) + BOARD_BORDER + WINDOW_BORDER
   for j in range(0, tilesAmount):
      posY = j*(TILE_SIZE+TILE_INTERSPACE) + BOARD_BORDER + WINDOW_BORDER
      pygame.draw.rect(DISPLAYSURF, GRAY, (posX, posY, TILE_SIZE, TILE_SIZE))

# Executa o game loop
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
   pygame.display.update()
