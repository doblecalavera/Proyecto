import random
import Entidad2

class Entidades:
    def __init__(self, mapa, n):
        self.entidades = []
        self.mapa = mapa
        self.crear_entidades(n)

    def crear_entidades(self, n):
        filas, columnas = self.mapa.shape
        for _ in range(n):
            pos_x = random.randint(0, filas - 1)
            pos_y = random.randint(0, columnas - 1)
            entidad = Entidad2.Entidad(pos_x, pos_y)
            self.entidades.append(entidad)

    def mover_todas(self):
        for entidad in self.entidades:
            entidad.mover(self.mapa)