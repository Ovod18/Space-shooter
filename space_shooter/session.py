"""This module defines the game session.

CLASSES

:py:class:`.Status`

FUNCTIONS

:py:func:`.init`

:py:func:`.wait`

|
"""

import personage
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
    personage.player.health = 100
    personage.player.lives = 3
    for mob in personage.mobs:
        mob.kill()
    personage.new_mob(40)


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
            if event.type == pygame.KEYUP:
                status.waiting = False
                status.game_over = False
                status.running = True
                init()

status = Status()
