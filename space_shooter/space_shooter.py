"""This module contains the main function of the space_hooter game.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.main`

CONSTANTS

:py:data:`.FPS`

|
"""

import pygame
import graphics
import personage
import collision
import session

FPS = 60
"""The frame rate.

|
"""

# Init the pygame and sounds.
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

def main():
    """The main function in space_shooter.

    |
    """
    session.init()
    session.wait()

    # Create the game cycle.
    while session.status.running:
        clock.tick(FPS)
        session.check_quit()
        personage.all_sprites.update(graphics.screen)
        collision.check_collision_all()
        session.check_game_over()
        # Rendering.
        graphics.draw_bg()
        personage.all_sprites.draw(graphics.screen)
        graphics.draw_player_info(personage.player, session.score)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
