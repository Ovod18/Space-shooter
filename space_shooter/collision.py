"""This module contains collision processing functions.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.mobs_bullets_collide`

:py:func:`.player_mobs_collide`

:py:func:`.check_collision_all`

|
"""

import pygame
import personage
import session

def mobs_bullets_collide(mobs, bullets):
    """This function defines mobs and bullets collision.

    :param: mobs: The group of mobs.

    :param: bullets: The group of bullets.

    |
    """
    hits = pygame.sprite.groupcollide(mobs, bullets,
                                      True, True)
    for hit in hits:
        personage.new_mob(1)
        session.score += 1

def player_mobs_collide(player, mobs):
    """This function defines player and mobs collision.

    :param: player: The instance of class Player in personage module.

    :param: mobs: The group of mobs.

    |
    """
    hits = pygame.sprite.spritecollide(personage.player, personage.mobs,
                                       True, pygame.sprite.collide_circle)
    for hit in hits:
        personage.player.health -= 10
        personage.new_mob(1)
        # Decrease player lives by 1.
        if personage.player.health  <= 0:
            personage.player.hide()
            personage.player.lives -= 1
            personage.player.health = 100

def check_collision_all():
    """Checking collision between all sprites and groups.

    |
    """
    mobs_bullets_collide(personage.mobs, personage.bullets)
    player_mobs_collide(personage.player, personage.mobs)
