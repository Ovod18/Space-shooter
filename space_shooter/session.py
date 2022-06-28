"""This module defines the game session.

CLASSES

:py:class:`.Status`

FUNCTIONS

:py:func:`.init`

:py:func:`.wait`

:py:func:`.check_quit`

:py:func:`.check_game_over`

|
"""

import sprite
import pygame
import graphics

waiting = True
running = False
game_over = False


class Status():
    """Status information of current game session.

     ATTRIBUTES

    .. py:attribute:: waiting
        The game current session status.
        :type: bool
    .. py:attribute:: running
        The game current session status.
        :type: bool
    .. py:attribute:: game_over
        The game current session status.
        :type: bool

    |
    """

    def __init__(self):
        self.waiting = True
        self.running = False
        self.game_over = False

def init():
    """Reset all to start.

    |
    """
    global score
    score = 0
    sprite.player.health = 100
    sprite.player.lives = 3
    for mob in sprite.mobs:
        mob.kill()
    sprite.new_mob(10)


def wait():
    """Waiting for player choice.

    |
    """
    graphics.draw_start_screen()
    pygame.display.flip()
    status.waiting = True
    while status.waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status.waiting = False
                status.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    status.waiting = False
                    status.game_over = False
                    status.running = True
                    init()

def check_quit():
    """Check the quit event.

    |
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status.running = False

def check_game_over():
    """Check is the game over.

    |
    """
    if sprite.player.lives == 0:
        status.game_over = True
        if status.game_over:
            wait()


status = Status()
