"""This module contains sprites difinitions.

:platform: Linux
:author: Ovod18

CLASSES

:py:class:`.Player`

:py:class:`.Mob`

:py:class:`.Bullet`

:py:class:`.Bonus`

FUNCTIONS

:py:func:`.new_mob`

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

bonuses = pygame.sprite.Group()
"""The group of all bonuses.

|
"""

class Player(pygame.sprite.Sprite):
    """This class defines the player.

    METHODS

    :py:meth:`Player.update()`

    :py:meth:`Player.shoot()`

    :py:meth:`Player.hide()`

    :py:meth:`Player.powerup()`

    |

    ATTRIBUTES

    .. py:attribute:: image
        The player image.
    .. py:attribute:: icon
        The player icon.
    .. py:attribute:: rect
        The rect of player surface.
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
        :type: bool
        :value: False
    .. py:attribute:: hide_timer
        Time of last player hiding.
        :type: int
    .. py:attribute:: power
        The player power.
        :type: int
        :value: 1
    .. py:attribute:: power_time
        The delay of power.
        :type: int
        :value: 5000

    |
    """

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = graphics.load_img("rocket.png")
        self.icon = pygame.transform.scale(self.image, (20, 25))
        # Check and draw collision area.
        #pygame.draw.circle(self.image, graphics.colors["BLACK"],
        #                   self.rect.center, self.radius)
        # Player rect.
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2
        self.rect.centerx = graphics.screen.get_width() / 2
        self.rect.bottom = graphics.screen.get_height() - 10
        self.speed_x = 0
        # Health.
        self.health = 100
        self.lives = 3
        # Visibility.
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        # Power
        self.power = 1
        self.power_time = 5000
        self.last_powerup = pygame.time.get_ticks()
        # Autoshooting.
        self.shoot_delay = 250
        self.last_shot = self.hide_timer
        self.add(all_sprites)

    def update(self, screen):
        """This method defines player updating.

        :param: screen: The player rendering screen.

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
        if keystate[pygame.K_SPACE]:
            self.shoot()
        now = pygame.time.get_ticks()
        if self.power > 1 and self.last_powerup < (now - self.power_time):
            self.power = 1
            self.last_powerup = now

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

        :param: args: Groups of sprites, where a bullet will be added.

        |
        """
        now = pygame.time.get_ticks()
        if not (self.hidden):
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                if self.power == 1:
                    bullet = Bullet(self.rect.centerx, self.rect.top)
                if self.power == 2:
                    bullet1 = Bullet((self.rect.centerx-self.rect.width/2),
                                                           self.rect.top)
                    bullet2 = Bullet((self.rect.centerx+self.rect.width/2),
                                                           self.rect.top)
                if self.power >= 3:
                    bullet1 = Bullet(self.rect.centerx, self.rect.top)
                    bullet2 = Bullet((self.rect.centerx-self.rect.width/2),
                                                           self.rect.top)
                    bullet3 = Bullet((self.rect.centerx+self.rect.width/2),
                                                           self.rect.top)

    def powerup(self):
        """This method defines player power up.

        |
        """
        self.last_powerup = pygame.time.get_ticks()
        if self.power < 3: self.power += 1

class Mob(pygame.sprite.Sprite):
    """This class defines a mob.

    METHODS

    :py:meth:`Mob.update()`

    :py:meth:`Mob.rotate()`

    |

    ATTRIBUTES

    .. py:attribute:: image_orig
        A mobs image.
    .. py:attribute:: image
        A copy of image_orig (for image rotation).
    .. py:attribute:: rect
        The rect of mob surface.
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
        self.image_orig = graphics.load_img("kal.png")
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
        self.add(all_sprites, mobs)

    def update(self, screen):
        """This method defines mob updating.

        :param: screen: The mob rendering screen.

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
        :type:
    .. py:attribute:: rect
        The rect of bullet surface.
        :type:
    .. py:attribute:: speed_y
        The speed of vertical bullet moving.
        :type: int

    |
    """

    def __init__(self, *pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = graphics.load_img("bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.bottom = pos
        self.speed_y = -10
        self.add(all_sprites, bullets)

    def update(self, screen):
        """This method defines bullet updating.

        |
        """
        self.rect.y += self.speed_y
        # Kill a bullet, if it goes upper the screen top.
        if self.rect.bottom < 0:
            self.kill()

def new_mob(count):
    """Generating new instance of class Mob in personage module.

    :param: count:Count to mobs generation.

    |
    """
    for i in range(count):
        mob = Mob(graphics.screen)

class Bonus(pygame.sprite.Sprite):
    """This class defines a bonus.

    METHODS

    :py:meth:`Bonus.update()`

    |

    ATTRIBUTES

    .. py:attribute:: rect
        The rect of bonus surface.
        :type:
    .. py:attribute:: speed_y
        The speed of vertical bonus moving.
        :type: int

    |
    """

    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = graphics.load_img("bonus.png")
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed_y = 2
        self.type = random.choice(("health", "power"))
        self.add(all_sprites, bonuses)

    def update(self, screen):
        """This method defines bonus updating.

        |
        """
        self.rect.y += self.speed_y
        # Kill a bonus, if it goes downer the screen bottom.
        if self.rect.top > graphics.HEIGHT:
            self.kill()

player = Player(graphics.screen)
