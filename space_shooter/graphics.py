"""This module defines the game graphics.

:platform: Linux
:author: Ovod18

FUNCTIONS

:py:func:`.draw_score`

:py:func:`.draw_health_bar`

:py:func:`.draw_lives`

:py:func:`.draw_bg`

CONSTANTS

:py:data:`.SCREEN_SIZE`

:py:data:`.FPS`

:py:data:`.IMG_DIR`

:py:data:`.colors`

|
"""

from os import path
import pygame

SCREEN_SIZE = (WIDTH := 400, HEIGHT := 600)
"""The screen size in px (WIDTH, HEIGHT)

|
"""

IMG_DIR = path.join(path.dirname(__file__), 'img')
"""The directory for loading images.

|
"""

colors = {"WHITE": (255, 255, 255), "BLACK": (0, 0, 0), "RED": (255, 0, 0),
          "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "YELLOW": (255, 255, 0)}
"""The dictionary of RGB colors.

|
"""

# Create the main window.
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Space_shooter")

bg_img = pygame.image.load(path.join(IMG_DIR, "background.png")).convert()
"""Background image.

|
"""

def draw_bg():
    """Rendering background.

    |
    """
    bg_rect = bg_img.get_rect()
    screen.blit(bg_img, bg_rect)

def draw_text(text, pos, size, color):
    """Writing text on the screen.

    |
    """
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (pos)
    screen.blit(text_surface, text_rect)

def draw_score(score):
    """Rendering text on the screen.

    :param: score: value for drowing
    :type: text: int

    |
    """
    draw_text(str(score), (pos := (WIDTH/2), 10), size := 18, colors["RED"])

def draw_health_bar(percent):
    """Rendering player health on the surface.

    :param: percent: percent of player health
    :type: percent: int

    |
    """
    pos = (5, 5)
    if percent < 0:
        percent = 0
    bar_size = (bar_length := 100, bar_height := 10)
    fill = (percent / 100) * bar_length
    if fill <= 30:
        color = colors["RED"]
    else:
        color = colors["GREEN"]
    border_rect = pygame.Rect(*pos, *bar_size)
    fill_rect = pygame.Rect(*pos, fill, bar_height)
    # Draw an internal rect.
    pygame.draw.rect(screen, color, fill_rect)
    # Draw a border.
    pygame.draw.rect(screen, colors["WHITE"], border_rect, 2)

def draw_lives(lives, icon):
    """Rendering player lives on the surface.

    :param: lives: number of lives
    :type: lives: int
    :param: icon: player icon
    :type: icon: object

    |
    """
    for i in range(lives):
        icon_pos = ((WIDTH - 80 + 25 * i), 5)
        screen.blit(icon, (icon_pos))

def draw_start_screen():
    """Rendering the start screen.

    |
    """
    """
    screen.blit(bg_img, bg_rect)
    draw_text(screen, "space shooter", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Arrow keys move, Space to fire", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press a key to begin", 18,
              WIDTH / 2, HEIGHT * 3 / 4)
    """
    pass
