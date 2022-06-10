# UAS Grafika Komputer
# Membuat Object 3D
# Nama  : Filza Hisana
# NIM   : 20051397018

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

# settings
screen_height = 800
screen_width = 600
line_colour = (0, 0, 0)


class Pyramid:

    # Membuat titik sudut piramid
    vertices = [
        [1, -1, -1],
        [1, -1, 1],
        [-1, -1, 1],
        [-1, -1, -1],
        [0, 1, 0]
    ]

    # Membuat rusuk piramid
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (1, 4),
        (1, 2),
        (2, 4),
        (2, 3),
        (3, 4)
    )

    # Membuat sisi piramid
    surfaces = (
        (1, 2, 4),
        (0, 1, 2, 3),
        (0, 1, 4),
        (2, 3, 4)
    )

# Memberi warna
    colors = (
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 50),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 50),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0))

    # Inisialisasi
    def __init__(self, scale=1):
        self.edges = Pyramid.edges
        self.vertices = list(numpy.multiply(
            numpy.array(Pyramid.vertices), scale))
        self.surfaces = Pyramid.surfaces

    # Menggambar piramid
    def draw(self):
        self.fill_sides()
        glLineWidth(5)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3f(1, 1, 1)
                glVertex3fv(self.vertices[vertex])
        glEnd()

    #  Memberi gerakan pada piramid
    def move(self, x, y, z):
        self.vertices = list(map(lambda vertex: (
            vertex[0] + x, vertex[1] + y, vertex[2] + z), self.vertices))

    # Mewarnai sisi - sisi piramid
    def fill_sides(self):
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            x = 0
            for vertex in surface:
                x += 1
                glColor3fv(Pyramid.colors[x]),
                glVertex3fv(self.vertices[vertex])
        glEnd()


def main():
    pygame.init()
    display = (screen_height, screen_width)
    # Seting pygame untuk 3d grafis
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    # Mengatur pergerakan z rotasi
    glTranslatef(0, 0, -20)

    # Menggambar pyramid sebagai object yang solid
    glEnable(GL_DEPTH_TEST)

    # Inisialisasi class pyramid
    p = Pyramid(2)

    velocity = 0.1

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        # Perputaran pyramid
        glRotatef(velocity * 10, 0, 1, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Memberi kontrol perputaran piramid pada keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            p.move(-velocity, 0, 0)
        if keys[pygame.K_RIGHT]:
            p.move(velocity, 0, 0)
        if keys[pygame.K_UP]:
            p.move(0, velocity, 0)
        if keys[pygame.K_DOWN]:
            p.move(0, -velocity, 0)
        if keys[pygame.K_w]:
            p.move(0, 0, velocity)
        if keys[pygame.K_s]:
            p.move(0, 0, -velocity)
        if keys[pygame.K_a]:
            glRotatef(-velocity*10, 0, 1, 0)
        if keys[pygame.K_d]:
            glRotatef(velocity*10, 0, 1, 0)

        # Untuk clear buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        p.draw()
        pygame.display.flip()


main()