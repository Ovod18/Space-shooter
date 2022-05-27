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
import space_shooter
import colors
import random
from os import path

IMG_DIR = path.join(path.dirname(__file__), 'img')

class Player(pygame.sprite.Sprite):
    """This class defines the player.

    METHODS

    :py:meth:`Player.update()`

    :py:meth:`Player.shoot()`

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
    .. py:attribute:: shield
        The player health.
        :type: int
        :value: 100

    |
    """

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR,
                                                 "rocket.png")).convert()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2
        # Check and draw collision area.
        #pygame.draw.circle(self.image, colors.RED,
        #                   self.rect.center, self.radius)
        screen_size = screen.get_size()
        screen_w = screen_size[0]
        screen_h = screen_size[1]
        self.rect.centerx = screen_w / 2
        self.rect.bottom = screen_h - 10
        self.speed_x = 0
        self.shield = 100

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

    def shoot(self, *args):
        """This method defines player shooting."""
        bullet = Bullet(self.rect.centerx, self.rect.top, args)
        return bullet

class Mob(pygame.sprite.Sprite):
    """This class defines a mob.

    METHODS

    :py:meth:`Mob.update()`

    :py:meth:`Mob.rotate()`

    |

    ATTRIBUTES

    .. py:attribute:: image_orig
        A mobs image.
        :type: object
    .. py:attribute:: image
        A copy of image_orig (for image rotation).
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
    .. py:attribute:: rot
        The initial rotation angle.
        :type: int
        :value: 0
    .. py:attribute:: rot_speed
        The angle of mob rotation.
        :type: int
    .. py:attribute:: last_update
        Time of mob updating.
        :type: int


    |
    """

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.image.load(path.join(IMG_DIR,
                                            "kal.png")).convert()
        self.image_orig.set_colorkey(colors.BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2
        # Check collision area.
        #pygame.draw.circle(self.image, colors.RED,
        #                   self.rect.center, self.radius)
        screen_size = screen.get_size()
        screen_w = screen_size[0]
        self.rect.x = random.randrange(screen_w - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-2, 2)
        self.speedy = random.randrange(1, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

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
        # Rotation.
        self.rotate()
        # Reloading when reaching the screen bottom.
        if ((self.rect.top > screen_h + 10) or
            (self.rect.left < -25) or
            (self.rect.right > screen_w + 20)):
            self.rect.x = random.randrange(screen_w - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 3)
            self.speedx = random.randrange(-2, 2)

    def rotate(self):
        """This method defines mob rotation.

        |
        """
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

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

    def __init__(self, x, y, *args):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR,
                                                 "bullet.png")).convert()
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = -10
        # Adding a bullet to groups (in args).
        for group in args:
            self.add(group)

    def update(self, screen):
        """This method defines bullet updating.

        |
        """
        self.rect.y += self.speed_y
        # Kill a bullet, if it goes upper the screen top.
        if self.rect.bottom < 0:
            self.kill()
