import numpy as np
import random

class EntidadSwarm():
    siguiente_id = 1000

    def __init__(self, pos_x, pos_y):
        self.id = EntidadSwarm.siguiente_id
        self.posicion = (pos_x, pos_y)
        self.velocidad = (0,0)
        EntidadSwarm.siguiente_id += 1

    def mover(self, centro, influencia_social, pos_obstaculo, separacion):
        vel_x = self.velocidad[0] - influencia_social*(self.posicion[0]-centro[0]) + 0.5*random.uniform(-1, 1)
        vel_y = self.velocidad[1] - influencia_social*(self.posicion[1]-centro[1]) + 0.5*random.uniform(1, 1)

        #si encuentra un obstáculo en separación de distancia se aplica una acaleración en sentido opuesto a donde está el obstáculo
        if(type(pos_obstaculo) != type(None)): 
            vel_x += 2*(separacion)/pos_obstaculo[0]
            vel_y += 2*(separacion)/pos_obstaculo[1]


        self.posicion = (self.posicion[0]+vel_x, self.posicion[1]+vel_y)
        self.velocidad = (vel_x, vel_y) 

    def mover2(self, centro, influencia_social, pos_obstaculo, separacion):
        # Calcular la diferencia de posición
        diff_x = self.posicion[0] - centro[0]
        diff_y = self.posicion[1] - centro[1]
    
        # Aplicar una función cuadrática a la magnitud de la influencia social y conservar el signo
        influencia_social_x = 0.05*influencia_social * (diff_x ** 2) * np.sign(diff_x) - 0.1 * np.sign(diff_x)
        influencia_social_y = 0.05*influencia_social * (diff_y ** 2) * np.sign(diff_y) - 0.1 * np.sign(diff_y)
    
        vel_x = self.velocidad[0] - influencia_social_x + 0.2*random.uniform(-1, 1)
        vel_y = self.velocidad[1] - influencia_social_y + 0.2*random.uniform(-1, 1)

        vel_x = min (abs(vel_x), 1) * np.sign(vel_x)
        vel_y = min (abs(vel_y), 1) * np.sign(vel_y)

        #si encuentra un obstáculo en separación de distancia se aplica una acaleración en sentido opuesto a donde está el obstáculo
        if(type(pos_obstaculo) != type(None)): 
            vel_x += (1/separacion)/(max(abs(self.posicion[0]-pos_obstaculo[0]), 0.001))*np.sign(vel_x)
            vel_y += (1/separacion)/(max(abs(self.posicion[1]-pos_obstaculo[1]), 0.001))*np.sign(vel_y)


        self.posicion = (self.posicion[0]+vel_x, self.posicion[1]+vel_y)
        self.velocidad = (vel_x, vel_y)
