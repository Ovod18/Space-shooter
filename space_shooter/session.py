"""This module defines the game session.

FUNCTIONS

:py:func:`.init`

|
"""

import personage

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
    personage.new_mob(10)
