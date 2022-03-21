"""This module contains the main function of the space_hooter game.

:platform: Linux
:author: Ovod18

    |
"""

import pygame
import random
import personage
import colors

WIDTH = 480
HEIGHT = 600
FPS = 60

# Setting colors.

def main():
    """The main function in space_shooter

    |
    """

    # Create the main window.
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space_shooter")
    clock = pygame.time.Clock()


    all_sprites = pygame.sprite.Group()
    player = personage.Player(screen)
    all_sprites.add(player)

    # Mobs generation.
    mobs = pygame.sprite.Group()
    for i in range(8):
        m = personage.Mob(screen)
        all_sprites.add(m)
        # Adding mob to the group.
        mobs.add(m)

    # Create the game cycle.
    running = True
    while running:
        clock.tick(FPS)
        # Check events
        for event in pygame.event.get():
            # Check closing main window event
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update(screen)

        # Check collision with player and mobs.
        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            running = False

        # Rendering
        screen.fill(colors.BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
