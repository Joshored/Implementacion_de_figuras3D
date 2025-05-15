import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cubo
import piramide
import esfera
import cilindro
import superEli

ancho, alto = 500, 500

# Variables globales para transformaciones
rotacion_x, rotacion_y = 0, 0
traslacion_x, traslacion_y, traslacion_z = 0, 0, 0
escala = 1.0
perspectiva = True
usar_textura = True
usar_iluminacion = False

def init_opengl():
    glClearColor(0.1, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)
    actualizar_proyeccion()
    
    # Configuración inicial de la luz
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    
    # Configuración de la luz 0
    luz_ambiental = [0.2, 0.2, 0.2, 1.0]
    luz_difusa = [0.8, 0.8, 0.8, 1.0]
    luz_especular = [1.0, 1.0, 1.0, 1.0]
    posicion_luz = [5.0, 5.0, 5.0, 0.0]
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiental)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    
    glEnable(GL_LIGHT0)
    if usar_iluminacion:
        glEnable(GL_LIGHTING)
    else:
        glDisable(GL_LIGHTING)

def actualizar_proyeccion():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    if perspectiva:
        gluPerspective(45, ancho / alto, 0.1, 100.0)
    else:
        glOrtho(-3 * ancho / alto, 3 * ancho / alto, -3, 3, 0.1, 100.0)
    
    glMatrixMode(GL_MODELVIEW)

def mostrar_menu_visual(pantalla):
    pantalla.fill((160, 195, 234))
    fuente = pygame.font.SysFont("Arial", 24)

    lineas = [
        "Tecla                       Acción",
        "1       Mostrar Cubo",
        "_________",
        "2       Mostrar Pirámide",
        "_________",
        "3       Mostrar Esfera",
        "_________",
        "4       Mostrar Cilindro",
        "_________",
        "5       Mostrar Superelipsoide",
        "_________",
        "6       Salir del programa"
    ]

    for i, texto in enumerate(lineas):
        render = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(render, (60, 50 + i * 35))

    pygame.display.flip()

def mostrar_menu():
    pygame.init()
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Menú de Figuras 3D")
    figura = None
    salir = False

    while not figura and not salir:
        mostrar_menu_visual(pantalla)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir = True
            elif evento.type == KEYDOWN:
                if evento.key == K_1:
                    figura = cubo
                elif evento.key == K_2:
                    figura = piramide
                elif evento.key == K_3:
                    figura = esfera
                elif evento.key == K_4:
                    figura = cilindro
                elif evento.key == K_5:
                    figura = superEli
                elif evento.key == K_6 or evento.key == K_ESCAPE:
                    salir = True
        pygame.time.wait(100)

    return figura

def main():
    global rotacion_x, rotacion_y, traslacion_x, traslacion_y, traslacion_z, escala
    global perspectiva, usar_textura, usar_iluminacion
    
    pygame.init()
    pantalla = None
    figura = None
    
    while True:
        # Mostrar menú y obtener selección
        figura = mostrar_menu()
        if not figura:
            # Si no hay figura seleccionada, salir del programa
            break
            
        # Crear una nueva ventana OpenGL
        if pantalla:
            pygame.display.quit()  # Cerrar ventana anterior si existe
        
        pantalla = pygame.display.set_mode((ancho, alto), DOUBLEBUF | OPENGL)
        pygame.display.set_caption("Implementación de una escena 3D realista con OpenGL")
        init_opengl()  # Reinicializar OpenGL
        
        # Resetear transformaciones
        rotacion_x, rotacion_y = 0, 0
        traslacion_x, traslacion_y, traslacion_z = 0, 0, 0
        escala = 1.0
        
        # Bandera para volver al menú
        volver_al_menu = False

        # Bucle de la figura actual
        while not volver_al_menu:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    # Salir completamente del programa
                    pygame.quit()
                    return
                elif evento.type == KEYDOWN:
                    # Controles de menú
                    if evento.key == K_ESCAPE:
                        # Volver al menú principal
                        volver_al_menu = True
                        break
                    
                    # Controles de transformación
                    elif evento.key == K_r:
                        # Reiniciar transformaciones
                        rotacion_x, rotacion_y = 0, 0
                        traslacion_x, traslacion_z = 0, 0
                        escala = 1.0
                    elif evento.key == K_p:
                        # Alternar proyección
                        perspectiva = not perspectiva
                        actualizar_proyeccion()
                    elif evento.key == K_t:
                        # Activar/desactivar textura
                        usar_textura = not usar_textura
                    elif evento.key == K_i:
                        # Activar/desactivar iluminación
                        usar_iluminacion = not usar_iluminacion
                        if usar_iluminacion:
                            glEnable(GL_LIGHTING)
                        else:
                            glDisable(GL_LIGHTING)
                    elif evento.key == K_PLUS or evento.key == K_KP_PLUS or evento.key == K_EQUALS:
                        # Aumentar escala
                        escala += 0.1
                    elif evento.key == K_MINUS or evento.key == K_KP_MINUS:
                        # Disminuir escala
                        escala = max(0.1, escala - 0.1)
                
               
            
            if volver_al_menu:
                break
                
            # Manejo de movimiento con WASD
            keys = pygame.key.get_pressed()
            
            # Teclas WASD para traslación
            # W: Hacia arriba (Y+), S: Hacia abajo (Y-)
            # A: Izquierda (X-), D: Derecha (X+)
            if keys[K_w]:
                traslacion_y += 0.1  # Movimiento hacia arriba
            if keys[K_s]:
                traslacion_y -= 0.1  # Movimiento hacia abajo
            if keys[K_a]:
                traslacion_x -= 0.1  # Movimiento hacia la izquierda
            if keys[K_d]:
                traslacion_x += 0.1  # Movimiento hacia la derecha
                
            # Teclas Q/E para controlar profundidad (Z)
            if keys[K_q]:
                traslacion_z -= 0.1  # Alejar (Z-)
            if keys[K_e]:
                traslacion_z += 0.1  # Acercar (Z+)
                
            # Rotación con teclas de flecha
            keys = pygame.key.get_pressed()
            if keys[K_UP]:
                rotacion_x += 1
            if keys[K_DOWN]:
                rotacion_x -= 1
            if keys[K_LEFT]:
                rotacion_y -= 1
            if keys[K_RIGHT]:
                rotacion_y += 1

            # Dibujar escena
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            
            # Aplicar transformaciones
            glTranslatef(traslacion_x, traslacion_y, -6 + traslacion_z)
            glRotatef(rotacion_x, 1, 0, 0)
            glRotatef(rotacion_y, 0, 1, 0)
            glScalef(escala, escala, escala)
            
            # Activar/desactivar textura según estado
            if usar_textura:
                glEnable(GL_TEXTURE_2D)
            else:
                glDisable(GL_TEXTURE_2D)
                
            # Dibujar la figura seleccionada
            figura.draw()

            pygame.display.flip()
            
            # Controlar la velocidad de fotogramas
            pygame.time.delay(10)

    # Asegurarse de que pygame se cierre correctamente
    pygame.quit()

if __name__ == "__main__":
    main()