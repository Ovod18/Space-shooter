"""This module contains interface rendering functions.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.draw_text`

:py:func:`.draw_shield_bar`

:py:func:`.draw_lives`

|
"""

import pygame
import colors

def draw_text(surface, text, size, x, y):
    """Rendering text on the surface.

    :param: surface: a surface for drowing text
    :type: surface: object
    :param: text: text for drowing
    :type: text: str
    :param: size: text size
    :type: size: int
    :param: x,y: the coordinates for drowing text
    :type: size: int

    |
    """
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, colors.RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x, y, pct):
    """Rendering player health on the surface.

    :param: surface: a surface for drowing text
    :type: surface: object
    :param: x,y: the coordinates for drowing text
    :type: x,y: int
    :param: pct: percent of player health
    :type: pct: int

    |
    """
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    if fill <= 30:
        color = colors.RED
    else:
        color = colors.GREEN
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, color, fill_rect)
    # Draw a border.
    pygame.draw.rect(surface, colors.WHITE, outline_rect, 2)

def draw_lives(surface, lives, img):
    """Rendering player lives on the surface.

    :param: surface: a surface for drowing lives
    :type: surface: object
    :param: lives: number of lives
    :type: lives: int
    :param: img: player icon
    :type: img: object

    |
    """
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = surface.get_width() - 80 + 25 * i
        img_rect.y = 5
        surface.blit(img, (img_rect.x, img_rect.y))
        """
        pygame.draw.circle(surface, colors.BLUE, (350+20*i, 10), 10)
        """
