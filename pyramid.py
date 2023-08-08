from OpenGL.GL import *

vertices = [
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (0, 1, 0)
]

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4)
]

faces = [
    (0, 1, 2, 3),
    (0, 1, 4),
    (1, 2, 4),
    (2, 3, 4),
    (3, 0, 4)
]

def draw_pyramid():
    glBegin(GL_QUADS)
    for face in faces:
        glColor3fv((0.7, 0.3, 0.3))
        for vertex_index in face:
            glVertex3fv(vertices[vertex_index])
    glEnd()

    glColor3fv((0, 0, 0))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex_index in edge:
            glVertex3fv(vertices[vertex_index])
    glEnd()
