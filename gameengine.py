#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys

import pygame
from pygame.locals import *

import random

import player

from defs import *
from board import Board, board

class GameEngine:
    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode((Board.GRID_SIZE * Board.BOARD_WIDTH,
                                          Board.GRID_SIZE * Board.BOARD_HEIGHT))
        pygame.display.set_caption('eSnejc')

        self.font = pygame.font.Font(None, 36)
        self.msg = ""

        screenw, screenh = screen.get_size()
        self.p1_score = 0
        self.p2_score = 0
        self.reset()

        self.fps_clock = pygame.time.Clock()
        self.is_running = True
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            self.fps_clock.tick(30)

    def reset(self):
        board.reset()

        self.player1 = player.Player(
                1,
                (Board.BOARD_WIDTH / 4, Board.BOARD_HEIGHT / 2),
                Direction.RIGHT,
                (255, 0, 0),
                {'LEFT': K_LEFT, 'RIGHT': K_RIGHT})

        self.player2 = player.Player(
                2,
                (Board.BOARD_WIDTH / 4 * 3, Board.BOARD_HEIGHT / 2),
                Direction.LEFT,
                (0, 0, 255),
                {'LEFT': K_a, 'RIGHT': K_d})

        for i in range(3, 0, -1):
            self.msg = "%d" % i
            self.handle_events()
            self.draw()
            pygame.time.delay(1000)

        self.msg = ""

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.quit()
                elif event.key == K_F1:
                    self.reset()

            self.player1.handle_events(event)
            self.player2.handle_events(event)

    def update(self):
        self.player1.update()
        self.player2.update()

        if not self.player1.is_alive or not self.player2.is_alive:
            if not self.player1.is_alive and not self.player2.is_alive:
                self.msg = "Total failure!"
            elif not self.player1.is_alive:
                self.msg = "Player 2 is victorious!"
                self.p2_score += 1
            elif not self.player2.is_alive:
                self.msg = "Player 1 is victorious!"
                self.p1_score += 1
            self.handle_events()
            self.draw()
            pygame.time.delay(2000)
            self.reset()

    def draw(self):
        pygame.display.get_surface().fill((0, 0, 0))

        board.draw()

        self.player1.draw()
        self.player2.draw()

        p1_score_text = self.font.render(
                "%d" % self.p1_score, 1, (255,255,255))
        p1_score_pos = p1_score_text.get_rect(
                centerx=64,
                centery=24)
        pygame.display.get_surface().blit(p1_score_text, p1_score_pos)

        p2_score_text = self.font.render(
                "%d" % self.p2_score, 1, (255,255,255))
        p2_score_pos = p2_score_text.get_rect(
                centerx=Board.BOARD_WIDTH * Board.GRID_SIZE - 64,
                centery=24)
        pygame.display.get_surface().blit(p2_score_text, p2_score_pos)

        rendered_msg = self.font.render(self.msg, 1, (255, 255, 255))
        msgpos = rendered_msg.get_rect(
                centery=Board.BOARD_HEIGHT * Board.GRID_SIZE / 2,
                centerx=Board.BOARD_WIDTH * Board.GRID_SIZE / 2)
        pygame.display.get_surface().blit(rendered_msg, msgpos)

        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit(0)

GameEngine()
