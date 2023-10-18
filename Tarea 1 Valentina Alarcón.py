import pyglet
import random
import numpy as np

# Primero crearemos la ventana
WIDTH = 1400
HEIGHT = 700
WINDOW_TITLE = "Tarea 1 Valentina Alarcón"
FULL_SCREEN = False
ventana = pyglet.window.Window(WIDTH, HEIGHT, WINDOW_TITLE, resizable =True)

ventana.set_fullscreen(FULL_SCREEN)

#Ahora, describiremos la forma de una nave mediante la creación de una clase, y las integraremos a un batch llamado "naves"
naves = pyglet.graphics.Batch()
class Nave:
    def __init__(self,j,k,col):
        self.triang_1 = pyglet.shapes.Triangle(x=j, y=k, x2=j+15, y2=k+15, x3=j+80, y3=k-65, color=col, batch=naves)
        self.triang_2 = pyglet.shapes.Triangle(x=j-60, y=k, x2=j-85, y2=k+15, x3=j-140, y3=k-65, color=col, batch=naves)
        self.triang_3 = pyglet.shapes.Triangle(x=j-29, y=k-40, x2=j-29, y2=k+120, x3=j, y3=k, color=(200,200,200), batch=naves)
        self.triang_4 = pyglet.shapes.Triangle(x=j-31, y=k-40, x2=j-31, y2=k+120, x3=j-60, y3=k, color=(200,200,200), batch=naves)
        self.triang_5 = pyglet.shapes.Triangle(x=j-10, y=k-10, x2=j-2, y2=k+55, x3=j+10, y3=k-70, color=(0,0,102), batch=naves)
        self.triang_6 = pyglet.shapes.Triangle(x=j+10, y=k, x2=j-2, y2=k+55, x3=j+10, y3=k-70, color=(0,0,102), batch=naves)
        self.triang_7 = pyglet.shapes.Triangle(x=j-50, y=k-10, x2=j-58, y2=k+55, x3=j-70, y3=k-70, color=(0,0,102), batch=naves)
        self.triang_8 = pyglet.shapes.Triangle(x=j-70, y=k, x2=j-58, y2=k+55, x3=j-70, y3=k-70, color=(0,0,102), batch=naves)

#Dibujaré 5 naves, siendo la nave 3 la lider
nave1= Nave(320,350,(153,153,255))
nave2= Nave(480,200,(255,51,153))
nave3= Nave(700,500,(204,255,153))
nave4= Nave(920,200,(153,204,255))
nave5= Nave(1080,350,(213,28,195))


#Ahora, describiremos la forma de una estrella en una clase y la integraremos a su propio batch llamado "estrellas"
estrellas = pyglet.graphics.Batch()

class Estrella:
    def __init__(self,j,k,col):
        self.body = pyglet.shapes.Star(x=j, y=k, outer_radius=20, inner_radius=5,rotation=0, num_spikes=4,color=col, batch=estrellas)
        self.advance = -1
        self.movement_speed = 5
        self.body.x = j
        self.body.y = k
    def update(self):
        self.body.y += self.advance*self.movement_speed
        if self.body.y <6:
            self.body.y +=799
        pass

#Creé una función que genera estrellas en posiciones aleatorias y las agrega a una lista
def genera_estrella():
    lista=[]
    for p in range(0,35):
        estrella_prueba_1= Estrella(random.randint(1,1600),random.randint(1,800),(224, 224, 224))
        estrella_prueba_2= Estrella(random.randint(1,1600),random.randint(1,800),(128, 128, 128))
        estrella_prueba_3= Estrella(random.randint(1,1600),random.randint(1,800),(204, 153, 255))
        lista.append(estrella_prueba_1)
        lista.append(estrella_prueba_2)
        lista.append(estrella_prueba_3)
    return lista

lista_estrellas = genera_estrella()
largo_lista = len(lista_estrellas)

#Finalmente, creamos el evento que dibujará la escena y actualizará la posición de las estrellas para crear el movimiento
@ventana.event
def on_draw():
    ventana.clear()
    for i in range(0,largo_lista):
        lista_estrellas[i].update()
    estrellas.draw()
    naves.draw()

pyglet.app.run()