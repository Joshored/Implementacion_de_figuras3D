from OpenGL.GL import *
from OpenGL.GLU import *
import textures

def draw():
    textura_id = textures.getTextura("talavera") 
    if textura_id:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textura_id)
    else:
        glDisable(GL_TEXTURE_2D)

    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE if textura_id else GL_FALSE)
    gluQuadricNormals(quadric, GLU_SMOOTH)

    # Dibuja el cilindro
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)  # Para ponerlo de pie (eje Z → Y)
    gluCylinder(quadric, 1.0, 1.0, 2.0, 32, 32)
    glPopMatrix()

    # Tapa inferior
    gluQuadricOrientation(quadric, GLU_INSIDE)
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    gluDisk(quadric, 0.0, 1.0, 32, 1)
    glPopMatrix()

    # Tapa superior
    gluQuadricOrientation(quadric, GLU_OUTSIDE)
    glPushMatrix()
    glTranslatef(0.0, 2.0, 0.0)
    glRotatef(-90, 1, 0, 0)
    gluDisk(quadric, 0.0, 1.0, 32, 1)
    glPopMatrix()

    glDisable(GL_TEXTURE_2D)
