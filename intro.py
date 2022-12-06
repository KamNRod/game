import pygame, sys
pygame.init() #Inicializamos la libreria. Se necesitan las dos lineas.

size = (800, 500) #Esto es una tupla donde coloco dos valores. Altura y anchura.

# Crear ventana
screen = pygame.display.set_mode(size) #Aca le estoy pasando la tupla al comando de crear pantalla. Y      ademas creo el objeto screen.

while True:
    for event in pygame.event.get():
        print(event) #Esto me va a dejar ver en tiempo real los eventos.
        if event.type == pygame.QUIT:
            sys.exit()

#Este while mantendra el juego abierto. El codigo en su interior es para registrar los eventos dentro del juego. En este caso, queremos registrar la X de la ventana para cerrarla. Por lo que registra la orden exit del sys.

#Esto es la estructura basica que necesitamos para todo.