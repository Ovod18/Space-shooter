"""This module contains the main function of the space_hooter game.

:platform: Linux
:author: Ovod18

    |
"""

import pygame
import random
from os import path
import personage
import colors
import interface

WIDTH = 400
HEIGHT = 600
FPS = 60


def bg_img_load():
    return pygame.image.load(path.join(img_dir, "background.png")).convert()

# Create the main window.
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space_shooter")
clock = pygame.time.Clock()

# Images directory.
img_dir = path.join(path.dirname(__file__), 'img')

# Loading graphics.
player_img = pygame.image.load(path.join(img_dir, "rocket.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "bullet.png")).convert()
mob_img = pygame.image.load(path.join(img_dir, "kal.png")).convert()
bg_img = bg_img_load()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

def new_mob(surface, img):
    # Mobs generation.
    m = personage.Mob(surface, img)
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

    player = personage.Player(screen, player_img)
    all_sprites.add(player)


    for i in range(8):
        new_mob(screen, mob_img)

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = player.shoot(bullet_img)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        all_sprites.update(screen)

        # Check collision with bullets and mobs.
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            m = personage.Mob(screen, mob_img)
            all_sprites.add(m)
            mobs.add(m)
            score += 1

        # Check collision with player and mobs.
        hits = pygame.sprite.spritecollide(player, mobs, False,
                                           pygame.sprite.collide_circle)
        if hits:
            running = False

        # Rendering
        #screen.fill(colors.BLACK)
        screen.blit(bg_img, bg_rect)
        all_sprites.draw(screen)
        interface.draw_text(screen, str(score), 18, WIDTH/2, 10)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
