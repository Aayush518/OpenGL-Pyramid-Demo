import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

observer = [5, 5, 5]
observer_speed = 0.1

perspective = True

def adjust_observer(key):
    global observer_speed
    if key == pygame.K_UP:
        observer[2] -= observer_speed
    elif key == pygame.K_DOWN:
        observer[2] += observer_speed
    elif key == pygame.K_LEFT:
        observer[0] -= observer_speed
    elif key == pygame.K_RIGHT:
        observer[0] += observer_speed

def toggle_projection(display):
    global perspective
    perspective = not perspective
    if perspective:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -15)
    else:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-10, 10, -10, 10, -50, 50)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

def rotate_scene(rotation_angle):
    glRotatef(rotation_angle, 1, 1, 1)
