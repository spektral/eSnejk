#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from defs import *
from board import Board, board

class Player:

    speed = 1
    size = 10

    def __init__(self, id, pos, direction, color, key_binds):
        self.id = id
        self.x, self.y = pos
        self.direction = direction
        self.color = color
        self.key_binds = key_binds
        self.track_color = map(lambda x: x / 2, self.color)
        self.is_alive = True

    def handle_events(self, event):
        if event.type == KEYDOWN:
            if event.key == self.key_binds['LEFT']:
                self.direction = (self.direction + 1) % 4
            if event.key == self.key_binds['RIGHT']:
                self.direction = (self.direction - 1) % 4

    def update(self):
        if self.is_alive:
            board.tiles[self.x][self.y] = self.id

            if (self.direction == Direction.UP):
                self.y = (self.y - self.speed) % Board.BOARD_HEIGHT
            if (self.direction == Direction.DOWN):
                self.y = (self.y + self.speed) % Board.BOARD_HEIGHT
            if (self.direction == Direction.LEFT):
                self.x = (self.x - self.speed) % Board.BOARD_WIDTH
            if (self.direction == Direction.RIGHT):
                self.x = (self.x + self.speed) % Board.BOARD_WIDTH

            if board.tiles[self.x][self.y] != 0:
                print("Player %d was eliminated!" % self.id)
                self.is_alive = False

    def draw(self):
        if self.is_alive:
            screen = pygame.display.get_surface()
            rect = pygame.Rect(Board.GRID_SIZE * self.x, Board.GRID_SIZE * self.y,
                               Board.GRID_SIZE, Board.GRID_SIZE)
            pygame.draw.rect(screen, self.color, rect)
