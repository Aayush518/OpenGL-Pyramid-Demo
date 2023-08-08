from OpenGL.GL import *

def draw_background():
    glClearColor(0.7, 0.7, 0.7, 1.0)  # Set gray background color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
