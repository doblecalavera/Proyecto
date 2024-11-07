import random
import numpy as np

class Entidad:
    siguiente_id = 1000
    pref = {0: 25}

    def __init__(self, pos_x, pos_y):
        self.id = Entidad.siguiente_id
        self.posicion = (pos_x, pos_y)
        self.velocidad_anterior = (0, 0)
        self.detenido = False
        self.duracion_parada = 0
        self.probabilidad_parada = 0.02
        Entidad.siguiente_id += 1

    def mover(self, m):
        if self.detenido:
            self.duracion_parada -= 1
            if self.duracion_parada <= 0:
                self.detenido = False
                self.probabilidad_parada = 0.1
            return

        opciones = np.array(['d', 'u', 'r', 'l'])
        preferencias = self.mvPosibles(m)
        if sum(preferencias) > 0:  # Asegurarse de que hay movimientos válidos
            if random.random() < self.probabilidad_parada:
                self.detenido = True
                self.duracion_parada = random.randint(1, 10)  # Duración aleatoria de la parada
                self.probabilidad_parada = 0.02  # Restablecer la probabilidad
            else:
                nueva_direccion = random.choices(opciones, preferencias)[0]
                if not self.es_opuesta(nueva_direccion):
                    self.moveAux(nueva_direccion, m)
                else:
                    # Si la nueva dirección es opuesta, elige otra dirección aleatoria
                    opciones = [op for op in opciones if not self.es_opuesta(op)]
                    if opciones:
                        self.moveAux(random.choice(opciones), m)
                self.probabilidad_parada += 0.02  # Incrementar la probabilidad de parar

    def moveAux(self, dir, m):
        nueva_posicion = list(self.posicion)
        if dir == 'd':
            nueva_posicion[0] += 1
        elif dir == 'u':
            nueva_posicion[0] -= 1
        elif dir == 'r':
            nueva_posicion[1] += 1
        elif dir == 'l':
            nueva_posicion[1] -= 1

        # Verificar si la nueva posición está dentro de los límites del mapa
        if 0 <= nueva_posicion[0] < m.shape[0] and 0 <= nueva_posicion[1] < m.shape[1]:
            self.posicion = tuple(nueva_posicion)
            self.actualizar_velocidad_anterior(dir)

    def mvPosibles(self, m):
        preferencias = [0, 0, 0, 0]  # Inicializar preferencias para 'd', 'u', 'r', 'l'
        x, y = self.posicion

        # Verificar si las posiciones adyacentes están dentro de los límites del mapa
        if x + 1 < m.shape[0]:
            preferencias[0] = Entidad.pref.get(m[x + 1, y], 0)  # 'd'
        if x - 1 >= 0:
            preferencias[1] = Entidad.pref.get(m[x - 1, y], 0)  # 'u'
        if y + 1 < m.shape[1]:
            preferencias[2] = Entidad.pref.get(m[x, y + 1], 0)  # 'r'
        if y - 1 >= 0:
            preferencias[3] = Entidad.pref.get(m[x, y - 1], 0)  # 'l'

        return preferencias

    def es_opuesta(self, dir):
        if dir == 'd' and self.velocidad_anterior == (-1, 0):
            return True
        elif dir == 'u' and self.velocidad_anterior == (1, 0):
            return True
        elif dir == 'r' and self.velocidad_anterior == (0, -1):
            return True
        elif dir == 'l' and self.velocidad_anterior == (0, 1):
            return True
        return False

    def actualizar_velocidad_anterior(self, dir):
        if dir == 'd':
            self.velocidad_anterior = (1, 0)
        elif dir == 'u':
            self.velocidad_anterior = (-1, 0)
        elif dir == 'r':
            self.velocidad_anterior = (0, 1)
        elif dir == 'l':
            self.velocidad_anterior = (0, -1)