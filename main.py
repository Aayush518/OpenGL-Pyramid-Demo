import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from pyramid import draw_pyramid
from observer import adjust_observer, toggle_projection, rotate_scene
from background import draw_background
from axes import draw_axes
from points import draw_points

def main():
    global display
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    toggle_projection(display)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.7, 0.7, 0.7, 1.0))
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # Fill polygons
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)

    rotation_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    toggle_projection(display)
                elif event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    adjust_observer(event.key)
                elif event.key == pygame.K_r:
                    rotation_angle += 2

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_background()
        draw_axes()
        rotate_scene(rotation_angle)  # Rotate the scene
        draw_pyramid()
        draw_points(rotation_angle)  # Pass rotation angle for points
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
