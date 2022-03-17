"""This module contains player difinitions.

:platform: Linux
:author: Ovod18

CLASSES

:py:class:`.Player`

    |
"""

import pygame
import colors

class Player(pygame.sprite.Sprite):
    """This class defines the player.

    METHODS

    :py:meth:`Player.update()`

    |

    ATTRIBUTES

    .. py:attribute:: image
        The player image.
        :type: object
    .. py:attribute:: rect
        The rect of player surface.
        :type: object
    .. py:attribute:: speed_x
        The speed of horizontal player  moving.
        :type: int
        :value: 8

    |
    """

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        screen_size = screen.get_size()
        screen_w = screen_size[0]
        screen_h = screen_size[1]
        self.image.fill(colors.GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_w / 2
        self.rect.bottom = screen_h - 10
        self.speed_x = 0

    def update(self, screen):
        """This method defines player updating.

        :param: object screen: The player rendering screen.

        |
        """
        screen_size = screen.get_size()
        screen_w = screen_size[0]
        screen_h = screen_size[1]
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 8
        if keystate[pygame.K_LEFT]:
            self.speed_x = -8
        self.rect.x += self.speed_x
        if self.rect.right > screen_w:
            self.rect.right = screen_w
        if self.rect.left < 0:
            self.rect.left = 0

