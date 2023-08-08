import pygame
from OpenGL.GL import *
from pyramid import vertices
from observer import observer

def draw_points(rotation_angle):
    for i, vertex in enumerate(vertices):
        text = f"V{i}"
        font = pygame.font.Font(None, 24)
        text_surface = font.render(text, True, (0, 0, 0))
        glColor3fv((0, 0, 0))
        glPushMatrix()
        glTranslatef(1.1 * vertex[0], 1.1 * vertex[1], 1.1 * vertex[2])
        glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tostring(text_surface, "RGBA", True))
        glPopMatrix()

    observer_text = "Observer"
    observer_font = pygame.font.Font(None, 24)
    observer_text_surface = observer_font.render(observer_text, True, (0, 0, 0))
    glColor3fv((0, 0, 0))
    glPushMatrix()
    glTranslatef(1.1 * observer[0], 1.1 * observer[1], 1.1 * observer[2])
    glDrawPixels(observer_text_surface.get_width(), observer_text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tostring(observer_text_surface, "RGBA", True))
    glPopMatrix()

    glColor3fv((1, 0, 0))
    glVertex3fv(observer)
