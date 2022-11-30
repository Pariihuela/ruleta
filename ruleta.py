#Importando pygame
import pygame as pg
import random

#Iniciando pygame
pg.init()

#Ancho y largo de Ventana
w = 1200
h = 800

pantalla = pg.display.set_mode((w, h))

#cargar imagen
icono = pg.image.load('src/icono.jpg')
fondo = pg.image.load('src/fondo.jpg')

#icono
pg.display.set_icon(icono)

#carga de imagenes de flecha
flecha = [
    pg.image.load('src/f1.png'),
    pg.image.load('src/f2.png'),
    pg.image.load('src/f3.png'),
    pg.image.load('src/f4.png'),
    pg.image.load('src/f5.png'),
    pg.image.load('src/f6.png'),
    pg.image.load('src/f7.png'),
    pg.image.load('src/f8.png')
]

reloj = pg.time.Clock()

fps = 240

#################################

cuenta = 0

reset = False

def recargarPantalla():
    aleatorio = random.randint(0,7)
    global cuenta
    global fps
    global reset

    pantalla.blit(fondo,[0,0])

    if reset and fps > 0:
        pantalla.blit(flecha[aleatorio],(430, 230))
        fps -= 1
        cuenta = aleatorio
    
    elif fps <= 0:
        pantalla.blit(flecha[cuenta],[430, 230])

#################################

game_over = False

while not game_over:

    #Bucle del juego
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True

    ######################################

    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE]:
        fps = 240
        reset = True

    ######################################

    pg.display.update()

    recargarPantalla()

    reloj.tick(fps)

pg.quit()