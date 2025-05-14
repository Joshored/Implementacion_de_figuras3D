from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import os
import textures

texturaPiramide = None

def draw():
    textura_id = textures.getTextura("talavera")
    if textura_id:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textura_id)
    else:
        glDisable(GL_TEXTURE_2D)

    glBegin(GL_TRIANGLES)

    # Cara frontal
    glTexCoord2f(0.5, 1.0)
    glVertex3f(0, 1, 0)     
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1, -1, 1)   
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1, -1, 1)    

    # Cara derecha
    glTexCoord2f(0.5, 1.0)
    glVertex3f(0, 1, 0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1, -1, 1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1, -1, -1)

    # Cara trasera
    glTexCoord2f(0.5, 1.0)
    glVertex3f(0, 1, 0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1, -1, -1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1, -1, -1)

    # Cara izquierda
    glTexCoord2f(0.5, 1.0)
    glVertex3f(0, 1, 0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1, -1, -1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1, -1, 1)
    glEnd()

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1, -1, 1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1, -1, 1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1, -1, -1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1, -1, -1)
    glEnd()

    glDisable(GL_TEXTURE_2D)
