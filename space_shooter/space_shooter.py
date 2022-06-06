"""This module contains the main function of the space_hooter game.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.main`

CONSTANTS

:py:data:`.FPS`

|
"""

from os import path
import pygame
import random
import graphics
import instances
import collision

FPS = 60
"""The frame rate.

|
"""

# Init the pygame and sounds.
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen = graphics.screen



def main():
    """The main function in space_shooter

    |
    """

    # Rendering background.
    graphics.draw_bg()
    pygame.display.flip()

    score = 0

    # The first instances.mobs.mobs generation.
    for i in range(9):
        instances.new_mob()

    # Create the game cycle.
    running = True
    while running:
        clock.tick(FPS)
        # Check events
        for event in pygame.event.get():
            # Check closing main window event
            if event.type == pygame.QUIT:
                running = False

        # Player shooting (if K_SPACE is pressed).
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
           instances.player.shoot(instances.all_sprites, instances.bullets)

        instances.all_sprites.update(graphics.screen)

        # Check collision with bullets and mobs.
        count = collision.mobs_bullets_collide(instances.mobs,
                                               instances.bullets)
        for i in range(count):
            instances.new_mob()
            score += 1

        # Check collision with player and mobs.
        collision.player_mobs_collide(instances.player, instances.mobs)
        # Game over.
        if instances.player.lives == 0:
            running = False

        # Rendering
        graphics.draw_bg()
        instances.all_sprites.draw(graphics.screen)
        graphics.draw_score(score)
        graphics.draw_health_bar(instances.player.health)
        graphics.draw_lives(instances.player.lives, instances.player.mini_img)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
