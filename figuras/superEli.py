from OpenGL.GL import *
import textures
import math

def signo(x):
    return 1 if x >= 0 else -1

def coseno_pot(u, m):
    return signo(math.cos(u)) * (abs(math.cos(u)) ** m)

def seno_pot(u, m):
    return signo(math.sin(u)) * (abs(math.sin(u)) ** m)

def draw(n1=0.5, n2=0.5, a=1.0, pasos_u=40, pasos_v=20):
    textura_id = textures.getTextura("roca")  # Usa cualquier textura
    if textura_id:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textura_id)
    else:
        glDisable(GL_TEXTURE_2D)

    for i in range(pasos_v):
        v0 = -math.pi / 2 + i * math.pi / pasos_v
        v1 = -math.pi / 2 + (i + 1) * math.pi / pasos_v

        glBegin(GL_TRIANGLE_STRIP)
        for j in range(pasos_u + 1):
            u = -math.pi + j * 2 * math.pi / pasos_u

            for v in [v0, v1]:
                x = a * coseno_pot(v, n1) * coseno_pot(u, n2)
                y = a * coseno_pot(v, n1) * seno_pot(u, n2)
                z = a * seno_pot(v, n1)

                s = (u + math.pi) / (2 * math.pi)  # textura coord
                t = (v + math.pi / 2) / math.pi

                glTexCoord2f(s, t)
                glVertex3f(x, y, z)
        glEnd()

    glDisable(GL_TEXTURE_2D)
