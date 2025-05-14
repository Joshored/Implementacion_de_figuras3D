from OpenGL.GL import *
from OpenGL.GLU import *
import textures

def draw():
    textura_id = textures.getTextura("aluminio")  
    if textura_id:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textura_id)
    else:
        glDisable(GL_TEXTURE_2D)

    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE if textura_id else GL_FALSE)
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluSphere(quadric, 1.0, 32, 32)

    glDisable(GL_TEXTURE_2D)
