import pygame as pg

from assets.scripts.locals import BASE_DIRECTORY


def render_text(message: str, font_size: int = 20, color: pg.Color = (255, 255, 255), font_name: str = "Jersey20", shadow_offset: int = 2) -> pg.Surface:
    font = pg.font.Font(BASE_DIRECTORY / "fonts" / font_name / "font.ttf", font_size)

    if shadow_offset:
        shadow = font.render(message, True, (0, 0, 0))
        text = font.render(message, True, color)

        surface = pg.Surface((text.get_width(), text.get_height()+shadow_offset), pg.SRCALPHA)
        surface.blit(shadow, (0, shadow_offset))
        surface.blit(text, (0, 0))

        del shadow, text

    else:
        surface = font.render(message, True, color)

    return surface
