from OpenGL.GL import *

vertices = [
    # Base vertices
    (-1, -1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, -1, -1),
    # Roof vertices
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0)
]

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4),
    (1, 5),
    (5, 6),
    (6, 2)
]

faces = [
    (0, 1, 5, 6),
    (0, 1, 2, 3),
    (4, 5, 6)
]

def draw_house():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex_index in edge:
            glVertex3fv(vertices[vertex_index])
    glEnd()
