from OpenGL.GL import *

def draw_axes():
    glBegin(GL_LINES)
    glColor3fv((1, 0, 0))  # Red x-axis
    glVertex3fv((0, 0, 0))
    glVertex3fv((10, 0, 0))
    glColor3fv((0, 1, 0))  # Green y-axis
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 10, 0))
    glColor3fv((0, 0, 1))  # Blue z-axis
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 0, 10))
    glEnd()
