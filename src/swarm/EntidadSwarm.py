import numpy as np
import random
import Swarm as Swarm

from Game_generation_utils import generator
import creaturesDict
import biomesCreatureRestriction as bcr

class EntidadSwarm():
    """
    Representa una particula perteneciente a un enjambre de particulas
    """
    def __init__(self, pos_x: float, pos_y: float, species: str):
        """
        posicion: x e y tonto :)
        velocidad: sabes lo que es
        rem_to_move: tuplas de dos componentes, 
            el primero indica el tiempo que va a estar parada la entidad, el segundo indica el tiempo en movimiento de la entidad
            p ej: (4,7) indica 4 iteraciones sin moverse y 7 en movimiento
            al iterar decremantamos, primero por la izq y luego por la dcha, al llegar a (0,0) reseteamos
        """
        self.posicion = (pos_x, pos_y)
        self.velocidad = (0,0)
        self.rem_to_move = (random.randint(4,7), random.randint(4,7))
        self.species = species

    def mover(self, centro: tuple[int, int], inf_soc: int, generador: generator):
        """
        Funcion que mueve la entidad:
        centro: tupla de dos componentes, indica el centro del enjambre
        inf_soc: influencia social, indica cuanto influye la posición del centro en la velocidad de la entidad
        generador: instancia del generador de terrenos, para chequear obstaculos y biomas
        """
        if self.rem_to_move == (0,0): #Si a la entidad se le acabo el tiempo de movimiento
            self.rem_to_move = (random.randint(4,7), random.randint(4,7))

        elif self.rem_to_move[0] == 0: # Si se le axabo el tiempo de estar parada
            self.rem_to_move = (0, self.rem_to_move[1]-1)

            # Calcular la diferencia de posición
            d_x_c = self.posicion[0] - centro[0]
            d_y_c = self.posicion[1] - centro[1]

            v_x = self.velocidad[0] - inf_soc * random.random() * d_x_c
            v_y = self.velocidad[1] - inf_soc * random.random() * d_y_c

            vel_x = min(abs(v_x), creaturesDict.creatures[self.species]["maxSpeed"]) * np.sign(v_x)
            vel_y = min(abs(v_y), creaturesDict.creatures[self.species]["maxSpeed"]) * np.sign(v_y)
            
            new_pos = (self.posicion[0] + vel_x, self.posicion[1] + vel_y)

            if generador.getBioma2(int(new_pos[0]),int(new_pos[1])) not in creaturesDict.creatures[self.species]["obstacleBiomes"]:
                if generador.isObject(int(new_pos[0]),int(new_pos[1])) != 1:
                    self.posicion = new_pos
                    self.velocidad = (vel_x, vel_y)
        else: #Si le queda tiempo de estar parada
            self.rem_to_move = (self.rem_to_move[0]-1, self.rem_to_move[1])

