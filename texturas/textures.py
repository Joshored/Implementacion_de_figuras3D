from OpenGL.GL import *
import pygame  
import os

texturasCargadas = {}

def cargarTextura (nombre, rutaRelativa):
    global texturasCargadas
    if nombre in texturasCargadas:
        return texturasCargadas[nombre]
    
    rutaAbsoluta = os.path.join(os.path.dirname(__file__), rutaRelativa)
    print("Cargando desde:", rutaAbsoluta) #comprobasion de la direccion de ruta
    superfice = pygame.image.load(rutaAbsoluta)
    datos = pygame.image.tostring(superfice, "RGB", True)
    ancho, alto = superfice.get_size()

    texturaID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texturaID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ancho, alto, 0, GL_RGB, GL_UNSIGNED_BYTE, datos)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    texturasCargadas[nombre] = texturaID
    return texturaID

def getTextura(nombre):
    return texturasCargadas.get(nombre, None)
