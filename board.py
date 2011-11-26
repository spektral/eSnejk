#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import pygame

class Board:

    GRID_SIZE = 8
    BOARD_WIDTH = 100
    BOARD_HEIGHT = 100

    def __init__(self):
        self.reset()

    def reset(self):
        self.tiles = []
        for y in range(self.BOARD_HEIGHT):
            self.tiles.append([])
            for x in range(self.BOARD_WIDTH):
                self.tiles[y].append(0)

    def draw(self):
        screen = pygame.display.get_surface()
        for y in range(self.BOARD_HEIGHT):
            for x in range(self.BOARD_WIDTH):
                if self.tiles[x][y] != 0:
                    if self.tiles[x][y] == 1:
                        color = (128, 0, 0)
                    elif self.tiles[x][y] == 2:
                        color = (0, 0, 128)
                    rect = pygame.Rect(self.GRID_SIZE * x, self.GRID_SIZE * y,
                                       self.GRID_SIZE, self.GRID_SIZE)
                    pygame.draw.rect(screen, color, rect)

board = Board()
