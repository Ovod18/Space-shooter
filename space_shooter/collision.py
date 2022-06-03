"""This module contains collision processing functions.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.mobs_bullets_collide`

:py:func:`.player_mobs_collide`

|
"""

import pygame
import instances

def mobs_bullets_collide(mobs, bullets):
    """This function defines mobs and bullets collision.

    :param: mobs: The group of mobs.

    :param: bullets: The group of bullets.

    |
    """
    hits = pygame.sprite.groupcollide(mobs, bullets,
                                      True, True)
    return len(hits)

def player_mobs_collide(player, mobs):
    """This function defines player and mobs collision.

    :param: player: The instance of class Player in personage module.

    :param: mobs: The group of mobs.

    |
    """
    hits = pygame.sprite.spritecollide(instances.player, instances.mobs,
                                       True, pygame.sprite.collide_circle)
    for hit in hits:
        instances.player.health -= 10
        instances.new_mob()
        # Decrease player lives by 1.
        if instances.player.health  <= 0:
            instances.player.hide()
            instances.player.lives -= 1
            instances.player.health = 100
