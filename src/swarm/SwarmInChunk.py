import random

import numpy as np
from Game_generation_utils import generator

import Swarm as Swarm
import biomesCreatureRestriction as bcr


def getChunkCreatures(generador: generator, x_in: np.int16, y_in: np.int16,min_swarms: np.uint8, max_swarms: np.uint8, tam_chunk: np.uint16):
    """
    Creamos un numero determinado de swarms por cada chunk, dependiendo del bioma sera de una especie o de otra
    si es un bioma sin especies, no generamos el swarm
    """
    n = random.randint(min_swarms,max_swarms) #Numero de swarms por chunk
    swarms = []
    for _ in range(n):
        ran_x = random.uniform(0,tam_chunk)
        ran_y = random.uniform(0,tam_chunk)
        posx = x_in*tam_chunk + ran_x
        posy = y_in*tam_chunk + ran_y
        biome = generador.getBioma2(np.int32(posx), np.int32(posy))

        list_creatures = list(bcr.creaturesBiomeRestriction[biome].keys())
        if len(list_creatures) != 0:
            list_prob = [bcr.creaturesBiomeRestriction[biome][creature] for creature in list_creatures]
            species = random.choices(list_creatures, weights=tuple(list_prob), k=1)[0]
            swarm = Swarm.Swarm((posx,posy),species, generador)
            swarms.append(swarm)
    return swarms
