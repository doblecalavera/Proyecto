from asyncio import sleep
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import Swarm, Entidad, Entidad2, Entidades


def testMove():
    lent = np.array([Entidad.Entidad(5, 5), Entidad.Entidad(8, 4), Entidad.Entidad(3,1)])
    for i in range(20):
        mapa = np.zeros((10, 10))
        for e in lent:
            e.mover()
            mapa[e.pos_x%10, e.pos_y%10] = e.id
            print(e.pos_x%10, e.pos_y%10)
        print(mapa)
        print("=================================================================")

def testMvPosibles():
    e = Entidad.Entidad(2, 1)
    mapa = np.zeros((5, 5))
    mapa[2,0] = -1
    mapa[3,1] = 5
    print(mapa)
    print(e.mvPosibles(mapa))

def testMoveV2():
    lent = np.array([Entidad.Entidad(5, 5), Entidad.Entidad(7, 4), Entidad.Entidad(1, 3), Entidad.Entidad(4, 6), Entidad.Entidad(8, 2),])
    mapa = np.zeros((10, 10))
    mapa[:mapa.shape[1], 0::mapa.shape[1]-1] = -1
    mapa[0::mapa.shape[0]-1, :mapa.shape[0]] = -1
    print()
    mapaAux = mapa.copy()

    for i in range(20):
        for e in lent:
            e.moveV2(mapaAux)
            mapaAux[e.pos_x%10, e.pos_y%10] = e.id
        print(mapaAux)
        mapaAux = mapa.copy()
        print("=================================================================")

def testMvPosiblesV2():
    lent = np.array([Entidad.Entidad(1, 1), Entidad.Entidad(3, 1)])
    mapa = np.zeros((10, 10))
    mapa[:mapa.shape[0], ::mapa.shape[1]-1] = -1
    mapa[::mapa.shape[0]-1, :mapa.shape[1]] = -1
    for e in lent: 
        mapa[e.pos_x, e.pos_y] = e.id
    print(mapa)

    for i in range(20):
        for e in lent: 
            mapa[e.pos_x, e.pos_y] = 0
            e.moveV3(mapa)
            mapa[e.pos_x, e.pos_y] = e.id

        print(mapa)
        #mapaAux = mapa.copy()
        print("=================================================================")

def visualizar_swarm():
    mapa = np.zeros((400, 400))
    #mapa[200,200] = 1
    centro = (200, 200)
    n = 1
    d = 10
    pasos = 500
    rango_movimiento = 30
    swarm = Swarm.Swarm(centro, n, d)
    visualizar_swarm_aux(mapa, swarm, pasos, rango_movimiento)

def visualizar_swarm_aux(mapa, swarm, pasos, rango_movimiento):
    plt.ion()
    fig, ax = plt.subplots()
    
    for paso in range(pasos):
        ax.clear()
        ax.set_xlim(swarm.centro[0] - rango_movimiento, swarm.centro[0] + rango_movimiento)
        ax.set_ylim(swarm.centro[1] - rango_movimiento, swarm.centro[1] + rango_movimiento)
        
        # Dibujar el punto centro
        ax.plot(swarm.centro[0], swarm.centro[1], 'ro', label='Centro')
        
        # Dibujar las entidades
        for entidad in swarm.entidades:
            ax.plot(entidad.posicion[0], entidad.posicion[1], 'bo')
        
        plt.legend()
        plt.draw()
        plt.pause(0.1)
        
        # Mover las entidades
        swarm.mover_entidades(mapa)
    
    plt.ioff()
    plt.show()

def actualizar(frame, entidades, scatter):
    entidades.mover_todas()
    posiciones = np.array([entidad.posicion for entidad in entidades.entidades])
    scatter.set_offsets(posiciones)
    return scatter,

def testEntidad2():
    mapa = np.zeros((10, 10))
    entidades = Entidades.Entidades(mapa, 10)

    fig, ax = plt.subplots()
    ax.set_xlim(0, mapa.shape[0])
    ax.set_ylim(0, mapa.shape[1])
    posiciones_iniciales = np.array([entidad.posicion for entidad in entidades.entidades])
    scatter = ax.scatter(posiciones_iniciales[:, 0], posiciones_iniciales[:, 1])

    ani = animation.FuncAnimation(fig, actualizar, fargs=(entidades, scatter), interval=500, blit=False)
    plt.show()

if __name__ == '__main__':
    #testEntidad2()
    visualizar_swarm()