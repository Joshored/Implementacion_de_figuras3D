# Implementacion_de_figuras3D
El desarrollo de gráficos tridimensionales representa una parte esencial en las aplicaciones modernas de simulación, videojuegos y diseño asistido por computadora. Esta práctica se enfoca en la construcción de una escena 3D interactiva 
utilizando tecnologías como Python, Pygame y PyOpenGL, incorporando técnicas clave para alcanzar un mayor realismo gráfico, 
como lo son la iluminación dinámica, texturas, uso del Z-buffer.

El objetivo principal fue integrar distintos elementos visuales para crear una experiencia inmersiva e interactiva, aprovechando el poder de la API OpenGL desde un entorno de desarrollo accesible como Python.

# Características

- Figuras 3D: esfera, cubo, superelipsoide, superficie 3D tipo malla
- Iluminación con `glLightfv`, `glEnable(GL_LIGHTING)` y materiales
- Texturizado con imágenes externas (JPEG/PNG) usando `glTexImage2D`
- Transformaciones: traslación, rotación, escalado
- Interfaz interactiva con menús en Pygame
- Proyecciones ortográficas y en perspectiva
- Z-buffer para ocultamiento de superficies
- 
#Requisitos

- Python 3.10
- Pygame
- PyOpenGL
- NumPy

## Instrucciones de uso
Ejecuta el archivo principal desde consola
python main.py
despues de la ejecucion aparece un menu en cual indica cual figura se desea mostrar
con las teclas 1,2,3 etc.

#controles
flechas: rotar objeto
+/-:escalar el objeto 
T: alternar textura
I: alternar iluminación
P: cambiar proyección 
1,2,3..:Cambiar figura a dibujar
Esc:Salir del programa


La práctica permitió integrar conocimientos fundamentales de la graficación 3D con herramientas modernas como PyOpenGL. Se comprobo que con Python es posible crear escenas interactivas y visualmente atractivas, siempre y cuando se dominen los principios de modelado geométrico, proyección, iluminación y texturizado*
