"""This module contains collision processing functions.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.mobs_bullets_collide`

:py:func:`.player_mobs_collide`

:py:func:`.player_bonuses_collide`

:py:func:`.check_collision_all`

|
"""

import pygame
import random
import sprite
import session

def mobs_bullets_collide(mobs, bullets):
    """This function defines mobs and bullets collision.

    :param: mobs: The group of mobs.

    :param: bullets: The group of bullets.

    |
    """
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        sprite.new_mob(1)
        session.score += 1
        if random.random() > 0.9: b = sprite.Bonus(hit.rect.center)

def player_mobs_collide(player, mobs):
    """This function defines player and mobs collision.

    :param: player: The instance of class Player in sprite module.

    :param: mobs: The group of mobs.

    |
    """
    hits = pygame.sprite.spritecollide(sprite.player, sprite.mobs,
                                       True, pygame.sprite.collide_circle)
    for hit in hits:
        sprite.player.health -= sprite.Mob.damage
        sprite.new_mob(1)
        # Decrease player lives by 1.
        if sprite.player.health  <= 0:
            sprite.player.hide()
            sprite.player.lives -= 1
            sprite.player.health = player.health_max

def player_bonuses_collide(player, bonuses):
    """This function defines player and bonuses collision.

    :param: player: The instance of class Player in sprite module.

    :param: mobs: The group of bonuses.

    |
    """
    hits = pygame.sprite.spritecollide(player, bonuses, True,
                                       pygame.sprite.collide_circle)
    for hit in hits:
        if hit.type == 'health': player.health = player.health_max
        elif hit.type == 'power': player.powerup()

def check_collision_all():
    """Checking collision between all sprites and groups.

    |
    """
    mobs_bullets_collide(sprite.mobs, sprite.bullets)
    player_mobs_collide(sprite.player, sprite.mobs)
    player_bonuses_collide(sprite.player, sprite.bonuses)
