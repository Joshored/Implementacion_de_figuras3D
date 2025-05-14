from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import os
import textures

texturaCubo = None

def draw():
    textura_id = textures.getTextura("roca")
    if textura_id:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textura_id)
    else:
        glDisable(GL_TEXTURE_2D)

    glBegin(GL_QUADS)

    # Cara frontal
    glTexCoord2f(0, 0); glVertex3f(-1, -1,  1)
    glTexCoord2f(1, 0); glVertex3f( 1, -1,  1)
    glTexCoord2f(1, 1); glVertex3f( 1,  1,  1)
    glTexCoord2f(0, 1); glVertex3f(-1,  1,  1)

    # Cara trasera
    glTexCoord2f(0, 0); glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0); glVertex3f( 1, -1, -1)
    glTexCoord2f(1, 1); glVertex3f( 1,  1, -1)
    glTexCoord2f(0, 1); glVertex3f(-1,  1, -1)

    # Cara izquierda
    glTexCoord2f(0, 0); glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0); glVertex3f(-1, -1,  1)
    glTexCoord2f(1, 1); glVertex3f(-1,  1,  1)
    glTexCoord2f(0, 1); glVertex3f(-1,  1, -1)

    # Cara derecha
    glTexCoord2f(0, 0); glVertex3f(1, -1, -1)
    glTexCoord2f(1, 0); glVertex3f(1, -1,  1)
    glTexCoord2f(1, 1); glVertex3f(1,  1,  1)
    glTexCoord2f(0, 1); glVertex3f(1,  1, -1)

    # Cara superior
    glTexCoord2f(0, 0); glVertex3f(-1, 1, -1)
    glTexCoord2f(1, 0); glVertex3f( 1, 1, -1)
    glTexCoord2f(1, 1); glVertex3f( 1, 1,  1)
    glTexCoord2f(0, 1); glVertex3f(-1, 1,  1)

    # Cara inferior
    glTexCoord2f(0, 0); glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0); glVertex3f( 1, -1, -1)
    glTexCoord2f(1, 1); glVertex3f( 1, -1,  1)
    glTexCoord2f(0, 1); glVertex3f(-1, -1,  1)

    glEnd()
    glDisable(GL_TEXTURE_2D)
