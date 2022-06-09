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

    # Primary rendering background.
    graphics.draw_bg()
    pygame.display.flip()

    session.init()
    session.wait()

    # Create the game cycle.
    while session.status.running:
        clock.tick(FPS)
        # Check events.
        for event in pygame.event.get():
            # Check closing main window event.
            if event.type == pygame.QUIT:
                session.status.running = False

        personage.all_sprites.update(graphics.screen)
        collision.check_collision_all()
        # Game over.
        if personage.player.lives == 0:
            #status.running = False
            session.status.game_over = True
            if session.status.game_over:
                session.wait()

        # Rendering.
        graphics.draw_bg()
        personage.all_sprites.draw(graphics.screen)
        graphics.draw_score(session.score)
        graphics.draw_health_bar(personage.player.health)
        graphics.draw_lives(personage.player.lives, personage.player.icon)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
