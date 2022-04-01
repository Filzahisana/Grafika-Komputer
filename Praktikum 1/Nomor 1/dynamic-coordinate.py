from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


koordinatx1 = input("Masukkan koordinat x1 : ")
koordinaty1 = input("Masukkan koordinat y1 : ")
koordinatx2 = input("Masukkan koordinat x2 : ")
koordinaty2 = input("Masukkan koordinat y2 : ")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-6, 6, -6, 6, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2f(float(koordinatx1), float(koordinaty1))
    glVertex2f(0.0, 0.00)
    glVertex2f(float(koordinatx2), float(koordinaty2))
    glEnd()

    glutSwapBuffers()


glutInit(sys.argv)
glutInitWindowSize(500, 500)
glutCreateWindow("No. 1 A")
glutDisplayFunc(draw)
glutMainLoop()
