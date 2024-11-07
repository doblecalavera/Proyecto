'''hacer que los bichos se queden parados de vez en cuando no aplicando la funcion siguiente siempre y
que cuando no se aplique se vayan frenando para que se queden x tiempo parados'''

import numpy as np
import Entidad2

class Swarm():
    siguiente_id = 100

    def __init__(self, centro, numero_entidades, distancia_max):
        self.id = Swarm.siguiente_id
        self.centro = centro
        self.entidades = []

        for c in (self.coordenadas_aleatorias(numero_entidades, distancia_max)):
            e = Entidad2.Entidad(c[0], c[1])
            self.entidades.append(e)

        Swarm.siguiente_id += 1

    def mover_entidades(self, mapa):
        for e in self.entidades: 
            e.mover(mapa)

    def mover_entidadesS(self, mapa):
        for e in self.entidades: 
            pos_obstaculo = self.obstaculo_cercano(e, mapa, 2)
            e.mover2(self.centro, 0.1, pos_obstaculo, 100)

    def obstaculo_cercano(self, entidad, mapa, distancia_max):
        filas, columnas = mapa.shape
        
        pos_obstaculo = None
        distancia_minima = float('inf')

        campo_de_vision = [(i, j) for i in range(-distancia_max, distancia_max) for j in range(-distancia_max, distancia_max) if abs(i) + abs(j) <= distancia_max]
        for p in campo_de_vision:
            nuevo_punto = np.array(entidad.posicion) + np.array(p)
            if 0 <= nuevo_punto[0] < filas and 0 <= nuevo_punto[1] < columnas:
                #cambiar 1 por cualquier indicacion de que una casilla es un obstaculo
                if mapa[int(nuevo_punto[0]), int(nuevo_punto[1])] == 1:
                    distancia = np.sum(np.abs(nuevo_punto - np.array(entidad.posicion)))
                    if distancia < distancia_minima:
                        distancia_minima = distancia
                        pos_obstaculo = nuevo_punto
                       
        return pos_obstaculo

    def coordenadas_aleatorias(self, numero, distancia_max):
        coordenadas = set()
        while len(coordenadas) < numero:
            coordenada = tuple(np.array(self.centro) + np.random.randint(-distancia_max, distancia_max + 1, size=2))
            coordenadas.add(coordenada)

        return coordenadas