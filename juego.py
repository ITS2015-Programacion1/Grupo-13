import pilasengine
import sys
import random

pilas = pilasengine.iniciar()





fondo = pilas.fondos.Fondo()
fondo.imagen = pilas.imagenes.cargar('imagenes/images.jpeg')

fondo.imagen.repetir_vertical = True
fondo.imagen.repetir_horizontal = True


def iniciar_juego():

    menu.eliminar()

    fondo = pilas.fondos.Fondo()
    fondo.imagen = pilas.imagenes.cargar('imagenes/Regal_Blue_Skulls.jpg')

    class MiProtagonista(pilasengine.actores.Actor):

        def iniciar(self):
            self.imagen = "imagenes/baby.png"
            self.escala = 0.25
            self.x = -250

        def actualizar(self):

            if pilas.control.izquierda:
                self.x -= 5

            elif pilas.control.derecha:
                self.x += 5

            elif pilas.control.arriba:
                self.y += 5

            elif pilas.control.abajo:
                self.y -= 5

    pilas.actores.vincular(MiProtagonista)
    protagonista = pilas.actores.MiProtagonista()
    protagonista.aprender(pilas.habilidades.LimitadoABordesDePantalla)



    class Enemigo(pilasengine.actores.Bomba):

        def iniciar(self):
            pilasengine.actores.Bomba.iniciar(self)
            self.izquierda = 320
            self.y = random.randint(-210, 210)

        def actualizar(self):
            self.x -= 5
            pilasengine.actores.Bomba.actualizar(self)



    enemigos = []

    def crear_enemigo():
        un_enemigo = Enemigo(pilas)
        enemigos.append(un_enemigo)
        return True

    pilas.tareas.agregar(3.3, crear_enemigo)


    def cuanto_toca_enemigo(protagonista, enemigo):
        protagonista.eliminar()
        enemigo.eliminar()

    pilas.colisiones.agregar(protagonista, enemigos, cuanto_toca_enemigo)




    class MiMunicion(pilasengine.actores.Actor):

        def iniciar(self):
            self.imagen = "disparos/bola_amarilla.png"

        def actualizar(self):
            self.escala = 1

    pilas.actores.vincular(MiMunicion)

    protagonista.aprender('disparar', municion='MiMunicion')

    bala = pilas.actores.MiMunicion()


    def bomba_explota(bala, enemigo):
        bala.eliminar()
        enemigo.explotar()
        enemigo.eliminar()

    pilas.colisiones.agregar(bala, enemigos, bomba_explota)





def salir_del_juego():
    sys.exit()



menu = pilas.actores.Menu(
        [
            ('Iniciar Juego', iniciar_juego),
            ('Salir', salir_del_juego),
        ])







pilas.ejecutar()
