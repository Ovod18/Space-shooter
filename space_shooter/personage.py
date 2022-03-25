"""This module contains player difinitions.

:platform: Linux
:author: Ovod18

CLASSES

:py:class:`.Player`

:py:class:`.Mob`

:py:class:`.Bullet`

|
"""

import pygame
import colors
import random


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
        The speed of horizontal player moving.
        :type: int
        :value: 8

    |
    """

    def __init__(self, screen, player_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        screen_size = screen.get_size()
        screen_w = screen_size[0]
        screen_h = screen_size[1]
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
            self.speed_x = 6
        if keystate[pygame.K_LEFT]:
            self.speed_x = -6
        self.rect.x += self.speed_x
        if self.rect.right > screen_w:
            self.rect.right = screen_w
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, bullet_img):
        bullet = Bullet(self.rect.centerx, self.rect.top, bullet_img)
        return bullet

class Mob(pygame.sprite.Sprite):
    """This class defines a mob.

    METHODS

    :py:meth:`Mob.update()`

    |

    ATTRIBUTES

    .. py:attribute:: image
        A mobs image.
        :type: object
    .. py:attribute:: rect
        The rect of mob surface.
        :type: object
    .. py:attribute:: speed_x
        The speed of horizontal mob  moving.
        :type: int
    .. py:attribute:: speed_y
        The speed of vertical mob moving.
        :type: int

    |
    """

    def __init__(self, screen, mob_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob_img
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        screen_size = screen.get_size()
        screen_w = screen_size[0]
        self.rect.x = random.randrange(screen_w - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-2, 2)
        self.speedy = random.randrange(1, 3)

    def update(self, screen):
        """This method defines mob updating.

        :param: object screen: The mob rendering screen.

        |
        """
        screen_size = screen.get_size()
        screen_w = screen_size[0]
        screen_h = screen_size[1]
        # Movement.
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Reloading when reaching the screen bottom.
        if ((self.rect.top > screen_h + 10) or
            (self.rect.left < -25) or
            (self.rect.right > screen_w + 20)):
            self.rect.x = random.randrange(screen_w - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 3)
            self.speedx = random.randrange(-2, 2)

class Bullet(pygame.sprite.Sprite):
    """This class defines a bullet.

    METHODS

    :py:meth:`Bullet.update()`

    |

    ATTRIBUTES

    .. py:attribute:: image
        A mobs image.
        :type: object
    .. py:attribute:: rect
        The rect of bullet surface.
        :type: object
    .. py:attribute:: speed_y
        The speed of vertical bullet moving.
        :type: int

    |
    """

    def __init__(self, x, y, bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = -10

    def update(self, screen):
        """This method defines bullet updating.

        |
        """
        self.rect.y += self.speed_y
        # Kill a bullet, if it goes upper the screen top.
        if self.rect.bottom < 0:
            self.kill()
