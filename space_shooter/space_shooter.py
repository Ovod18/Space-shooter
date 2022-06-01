"""This module contains the main function of the space_hooter game.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.new_mob`

:py:func:`.main`

CONSTANTS

:py:data:`.WIDTH`

:py:data:`.HEIGHT`

:py:data:`.FPS`

:py:data:`.IMG_DIR`

|
"""

import pygame
import random
from os import path
import personage
import colors
import interface

WIDTH = 400
"""The screen width in pixels."""

HEIGHT = 600
"""The screen height in pixels."""

FPS = 60
"""The frame rate."""

IMG_DIR = path.join(path.dirname(__file__), 'img')
"""The directory for loading images."""

# Create the main window.
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space_shooter")
clock = pygame.time.Clock()

bg_img = pygame.image.load(path.join(IMG_DIR, "background.png")).convert()

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
    bg_rect = bg_img.get_rect()
    screen.blit(bg_img, bg_rect)
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

        # Player shooting.
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
            player.shield -= 10
            new_mob(screen)
            # Decrease player lives by 1.
            if player.shield <= 0:
                player.hide()
                player.lives -= 1
                player.shield = 100
            # Game over.
            if player.lives == 0:
                running = False

        # Rendering
        #screen.fill(colors.BLACK)
        screen.blit(bg_img, bg_rect)
        all_sprites.draw(screen)
        interface.draw_text(screen, str(score), 18, WIDTH/2, 10)
        interface.draw_shield_bar(screen, 5, 5, player.shield)
        interface.draw_lives(screen, player.lives, player.mini_img)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
