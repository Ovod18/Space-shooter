"""This module defines the game graphics.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.draw_score`

:py:func:`.draw_health_bar`

:py:func:`.draw_lives`

:py:func:`.draw_bg`

CONSTANTS

:py:data:`.WIDTH`

:py:data:`.HEIGHT`

:py:data:`.FPS`

:py:data:`.IMG_DIR`

|
"""

from os import path
import pygame
import colors

WIDTH = 400
"""The screen width in pixels."""

HEIGHT = 600
"""The screen height in pixels."""

IMG_DIR = path.join(path.dirname(__file__), 'img')
"""The directory for loading images."""

# Create the main window.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space_shooter")

bg_img = pygame.image.load(path.join(IMG_DIR, "background.png")).convert()
"""Background image."""

def draw_bg():
    """Rendering background.

    |
    """
    bg_rect = bg_img.get_rect()
    screen.blit(bg_img, bg_rect)

def draw_score(score):
    """Rendering text on the screen.

    :param: score: value for drowing
    :type: text: int

    |
    """
    x = WIDTH / 2
    y = 10
    size = 18
    score = str(score)
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(score, True, colors.RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def draw_health_bar(percent):
    """Rendering player health on the surface.

    :param: percent: percent of player health
    :type: percent: int

    |
    """
    x = 5
    y = 5
    if percent < 0:
        percent = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (percent / 100) * BAR_LENGTH
    if fill <= 30:
        color = colors.RED
    else:
        color = colors.GREEN
    border_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(screen, color, fill_rect)
    # Draw a border.
    pygame.draw.rect(screen, colors.WHITE, border_rect, 2)

def draw_lives(lives, icon):
    """Rendering player lives on the surface.

    :param: lives: number of lives
    :type: lives: int
    :param: icon: player icon
    :type: icon: object

    |
    """
    for i in range(lives):
        icon_rect = icon.get_rect()
        icon_rect.x = WIDTH - 80 + 25 * i
        icon_rect.y = 5
        screen.blit(icon, (icon_rect.x, icon_rect.y))
