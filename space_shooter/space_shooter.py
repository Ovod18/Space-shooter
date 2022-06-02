"""This module contains the main function of the space_hooter game.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.new_mob`

:py:func:`.main`

|
"""

from os import path
import pygame
import random
import personage
import colors
import graphics

FPS = 60
"""The frame rate."""

# Init the pygame and sounds.
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen = graphics.screen

# Creating sprites groups.
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

def new_mob(surface):
    """Generating new mob.

    :param: surface: a surface for generating new mob
    :type: surface: object

    |
    """
    # Mobs generation.
    m = personage.Mob(surface)
    all_sprites.add(m)
    # Adding mob to the group.
    mobs.add(m)


def main():
    """The main function in space_shooter

    |
    """

    # Rendering background.
    graphics.draw_bg()
    pygame.display.flip()

    player = personage.Player(screen)
    all_sprites.add(player)


    for i in range(8):
        new_mob(screen)

    score = 0

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
            player.shoot(all_sprites, bullets)

        all_sprites.update(screen)

        # Check collision with bullets and mobs.
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            m = personage.Mob(screen)
            all_sprites.add(m)
            mobs.add(m)
            score += 1

        # Check collision with player and mobs.
        hits = pygame.sprite.spritecollide(player, mobs, True,
                                           pygame.sprite.collide_circle)
        for hit in hits:
            player.health -= 10
            new_mob(screen)
            # Decrease player lives by 1.
            if player.health  <= 0:
                player.hide()
                player.lives -= 1
                player.health = 100
            # Game over.
            if player.lives == 0:
                running = False

        # Rendering
        graphics.draw_bg()
        all_sprites.draw(screen)
        graphics.draw_text(screen, str(score), 18, graphics.WIDTH/2, 10)
        graphics.draw_health_bar(screen, 5, 5, player.health)
        graphics.draw_lives(screen, player.lives, player.mini_img)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
