"""This module contains instances and its groups
of classes in personage module.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.new_mob`

OBJECTS

:py:data:`.all_sprites`

:py:data:`.mobs`

:py:data:`.bullets`

:py:data:`.player`

|
"""

import pygame
import personage
import graphics


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
player = personage.Player(graphics.screen)
"""The instance of class Player in personage module."""
all_sprites.add(player)

def new_mob():
    """Generating new instance of class Mob in personage module.

    |
    """
    # Mobs generation.
    m = personage.Mob(graphics.screen)
    all_sprites.add(m)
    # Adding mob to the group.
    mobs.add(m)
