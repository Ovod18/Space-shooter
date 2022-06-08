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

    # Rendering background.
    graphics.draw_bg()
    pygame.display.flip()

    session.init()

    # The first mobs generation.
    #personage.new_mob(mobs_count := 30)

    # Create the game cycle.
    running = True
    game_over = False
    graphics.draw_start_screen()
    while running:
        clock.tick(FPS)
        # Check events.
        for event in pygame.event.get():
            # Check closing main window event.
            if event.type == pygame.QUIT:
                running = False

        # Player shooting (if K_SPACE is pressed).
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
           personage.player.shoot()

        personage.all_sprites.update(graphics.screen)

        # Check collision with bullets and mobs.
        collision.mobs_bullets_collide(personage.mobs,
                                               personage.bullets)
        # Check collision with player and mobs.
        collision.player_mobs_collide(personage.player, personage.mobs)
        # Game over.
        if personage.player.lives == 0:
            #running = False
            game_over = True
            if game_over:
                graphics.draw_start_screen()
                pygame.display.flip()
                waiting = True
                while waiting:
                    clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            waiting = False
                            running = False
                        if event.type == pygame.KEYUP:
                            waiting = False
                            game_over = False
                            session.init()
        # Rendering.
        graphics.draw_bg()
        personage.all_sprites.draw(graphics.screen)
        graphics.draw_score(session.score1)
        graphics.draw_health_bar(personage.player.health)
        graphics.draw_lives(personage.player.lives, personage.player.icon)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
