"""This module contains functions for drawing game interface.

:platform: Linux
:author: Ovod18

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

