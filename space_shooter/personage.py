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
import graphics
import random
from os import path

all_sprites = pygame.sprite.Group()
"""The group of all sprites.

|
"""
mobs = pygame.sprite.Group()
"""The group of mobs.

|
"""
bullets = pygame.sprite.Group()
"""The group of all bullets.

|
"""

class Player(pygame.sprite.Sprite):
    """This class defines the player.

    METHODS

    :py:meth:`Player.update()`

    :py:meth:`Player.shoot()`

    :py:meth:`Player.hide()`


    |

    ATTRIBUTES

    .. py:attribute:: image
        The player image.
        :type: object
    .. py:attribute:: mini_image
        The player icon.
        :type: object
    .. py:attribute:: rect
        The rect of player surface.
        :type: object
    .. py:attribute:: speed_x
        The speed of horizontal player moving.
        :type: int
        :value: 8
    .. py:attribute:: health
        The player health.
        :type: int
        :value: 100
    .. py:attribute:: shoot_delay
        Delay between shots.
        :type: int
        :value: 250
    .. py:attribute:: last_shot
        Time of last shot.
        :type: int
    .. py:attribute:: lives
        Count of player lives.
        :type: int
        :value: 3
    .. py:attribute:: hidden
        The flag of player hiding.
        :type: boolean
        :value: False
    .. py:attribute:: hide_timer
        Time of last player hiding.
        :type: int

    |
    """

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # Loading player image.
        self.image = pygame.image.load(path.join(graphics.IMG_DIR,
                                                 "rocket.png")).convert()
        self.image.set_colorkey(graphics.colors["BLACK"])
        # Loading player mini image.
        self.mini_img = pygame.transform.scale(self.image, (25, 19))
        self.mini_img.set_colorkey(graphics.colors["BLACK"])
        # Check and draw collision area.
        #pygame.draw.circle(self.image, graphics.colors["BLACK"],
        #                   self.rect.center, self.radius)
        # Player rect.
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2
        self.rect.centerx = graphics.screen.get_width() / 2
        self.rect.bottom = graphics.screen.get_height() - 10
        self.speed_x = 0
        # Player health.
        self.health = 100
        self.lives = 3
        # Player visibility.
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        # Autoshooting.
        self.shoot_delay = 250
        self.last_shot = self.hide_timer

    def update(self, screen):
        """This method defines player updating.

        :param: object screen: The player rendering screen.

        |
        """
        # Show the player in start point, if it is hidden. 
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = graphics.screen.get_width() / 2
            self.rect.bottom = graphics.screen.get_height() - 10

        screen_size = screen.get_size()
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 6
        if keystate[pygame.K_LEFT]:
            self.speed_x = -6
        self.rect.x += self.speed_x
        if self.rect.right > graphics.screen.get_width():
            self.rect.right = graphics.screen.get_width()
        if self.rect.left < 0:
            self.rect.left = 0
        #if keystate[pygame.K_SPACE]:
        #    self.shoot()

    def hide(self):
        """This method defines player hiding.

        |
        """
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (graphics.screen.get_width() / 2,
                            graphics.screen.get_height() + 200)

    def shoot(self):
        """This method defines player shooting.

        :param: object args: Groups of sprites, where a bullet will be added.

        |
        """
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)

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
        self.image_orig = pygame.image.load(path.join(graphics.IMG_DIR,
                                            "kal.png")).convert()
        self.image_orig.set_colorkey(graphics.colors["BLACK"])
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2
        # Check collision area.
        #pygame.draw.circle(self.image, graphics.colors["RED"],
        #                   self.rect.center, self.radius)
        screen_size = screen.get_size()
        self.rect.x = random.randrange(graphics.screen.get_width()
                                       - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-2, 2)
        self.speedy = random.randrange(1, 5)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def update(self, screen):
        """This method defines mob updating.

        :param: object screen: The mob rendering screen.

        |
        """
        screen_size = screen.get_size()
        # Movement.
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Rotation.
        self.rotate()
        # Reloading when reaching the screen bottom.
        if ((self.rect.top > graphics.screen.get_height() + 10) or
            (self.rect.left < -25) or
            (self.rect.right > graphics.screen.get_width() + 20)):
            self.rect.x = random.randrange(graphics.screen.get_width()
                                           - self.rect.width)
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

    def __init__(self, *pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(graphics.IMG_DIR,
                                                 "bullet.png")).convert()
        self.image.set_colorkey(graphics.colors["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.bottom = pos
        self.speed_y = -10
        # Adding a bullet to groups (in args).
        self.add(all_sprites, bullets)

    def update(self, screen):
        """This method defines bullet updating.

        |
        """
        self.rect.y += self.speed_y
        # Kill a bullet, if it goes upper the screen top.
        if self.rect.bottom < 0:
            self.kill()

def new_mob():
    """Generating new instance of class Mob in personage module.

    |
    """
    # Mobs generation.
    m = Mob(graphics.screen)
    all_sprites.add(m)
    # Adding mob to the group.
    mobs.add(m)

player = Player(graphics.screen)
all_sprites.add(player)
