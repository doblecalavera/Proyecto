import random

from Game_generation_utils import generator
import numpy as np

from EntidadSwarm import EntidadSwarm 
import creaturesDict

class Swarm():
    """
    Representa un conjunto de entidades
    """

    def __init__(self, centro: tuple[float, float], species: str, generador: generator):
        self.species = species
        self.centro = centro
        self.rem_to_move_center = random.randint(40,60)
        numero_entidades = random.randint(
            creaturesDict.creatures[self.species]["minPerSwarm"],
            creaturesDict.creatures[self.species]["maxPerSwarm"]
        )
        entidades = []
        for _ in range(numero_entidades):
            posx =  centro[0] + random.uniform(-16,16)
            posy =  centro[1] + random.uniform(-16,16)
            if generador.isObject(int(posx), int(posy)) or generador.getBioma2(int(posx), int(posy)) in creaturesDict.creatures[self.species]["obstacleBiomes"]:
                continue
            else:
                entidades.append(EntidadSwarm(posx, posy, species))
        self.entidades = entidades
        self.inf_soc = creaturesDict.creatures[self.species]["inf_soc"]

    def mover_entidades(self, generador: generator) -> None:
        if(self.rem_to_move_center==0):
            if(len(self.entidades)>0):
                nuevo_centro = random.choice(self.entidades).posicion
                nuevo_centro = (nuevo_centro[0]+ random.uniform(-4,4),nuevo_centro[1]+ random.uniform(-4,4))
                self.centro = nuevo_centro
                print(f"{self.species} - {int(self.centro[0]), int(self.centro[1])}: {generator.BIOMAS[generador.getBioma2(nuevo_centro[0],nuevo_centro[1])][1]}")
            self.rem_to_move_center = 50
        for e in self.entidades:
            e.mover(self.centro, self.inf_soc, generador)
        self.rem_to_move_center-=1


