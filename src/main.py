import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "HIDE"
import pygame as pg

import ui

GAME_VERSION = "[InDev]"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pg.init()

running = True
scene_name = "START"
scene_created = False
window_size = (1400, 800)

image = ui.render_text("C", 64, (255, 128, 8))
image_size = max(image.get_width(), image.get_height())
surface = pg.Surface((image_size, image_size), pg.SRCALPHA)
surface.blit(image, image.get_rect(center=(surface.get_width()//2, surface.get_height()//2)))
pg.display.set_icon(surface)
del image, image_size, surface

pg.display.set_caption(f"Controlador de Tráfego v{GAME_VERSION}")
screen = pg.display.set_mode(window_size, pg.RESIZABLE)

while running:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            pass

        elif event.type == pg.MOUSEBUTTONUP:
            pass

        elif event.type == pg.KEYDOWN:
            pass

        elif event.type == pg.KEYUP:
            pass

        elif event.type == pg.VIDEORESIZE:
            pass

        elif event.type == pg.QUIT:
            running = False

    if scene_name == "START":
        if not scene_created:
            scene_created = True

            screen.fill((180, 150, 120))

            line_1 = ui.render_text("CONTROLADOR DE", 40, shadow_offset=4)
            line_2 = ui.render_text("TRÁFEGO", 80, shadow_offset=8)
            line_spacement = -10
            header = pg.Surface((max(line_1.get_width(), line_2.get_width()), line_1.get_height()+line_2.get_height()+line_spacement), pg.SRCALPHA)
            header.blit(line_1, line_1.get_rect(midtop=(header.get_width()//2, 0)))
            header.blit(line_2, line_2.get_rect(midtop=(header.get_width()//2, line_1.get_height()+line_spacement)))

            screen.blit(header, header.get_rect(midtop=(window_size[0]//2, 20)))

            pg.display.flip()

pg.quit()
