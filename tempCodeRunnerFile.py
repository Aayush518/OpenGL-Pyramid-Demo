import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from house import draw_house, vertices  # Import the vertices list
from observer import adjust_observer, toggle_projection
from background import draw_background
from axes import draw_axes
from points import draw_points

def main():
    global display
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    toggle_projection()  # Set initial projection mode

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    toggle_projection()
                elif event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    adjust_observer(event.key)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_background()
        draw_axes()
        draw_house()  # Draw the 3D house
        draw_points(vertices)  # Pass the vertices list as an argument
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
