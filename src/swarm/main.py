import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from Game_generation_utils import generator
import plotly.express as px


import Swarm as Swarm, SwarmInChunk as SwarmInChunk

#Importante
#Si da error cometa esta linea
matplotlib.use('TkAgg')

dic_colors = {"Cerdo":'mo',"Pollo":'yo',"Zorro":'ko',"Pez":'bo',"Cabra":'co'}
a = generator(
    seedTemp=13532,
    seedAltu=131312,
    seedHume=31253,
    seedRios=31234,
    tamRios=7,
    varRios=128
    )
a.representation((-1,9),(-1,9))

CHUNK_COORDS = (0,0)
SWARMS_AMMOUNT = (4,8)
CHUNK_SIZE = 512

def visualizar_swarms():
    swarms = SwarmInChunk.getChunkCreatures(a, CHUNK_COORDS[0],CHUNK_COORDS[1],SWARMS_AMMOUNT[0],SWARMS_AMMOUNT[1],CHUNK_SIZE)
    visualizar_swarms_aux(swarms)

def visualizar_swarms_aux(swarms):
    plt.ion()
    _ , ax = plt.subplots()
    representation(a, (
            CHUNK_COORDS[0], 
            (CHUNK_COORDS[0] + (CHUNK_SIZE//128))
            ), 
        (
            CHUNK_COORDS[1], 
            (CHUNK_COORDS[1] + (CHUNK_SIZE//128))
        ))
    bg = plt.imread("newplot.png")
    while True:
        ax.clear()
        ax.set_xlim(CHUNK_SIZE*CHUNK_COORDS[0], CHUNK_SIZE*CHUNK_COORDS[0]+CHUNK_SIZE)
        ax.set_ylim(CHUNK_SIZE*CHUNK_COORDS[1], CHUNK_SIZE*CHUNK_COORDS[1]+CHUNK_SIZE)

        ax.imshow(np.fliplr(np.rot90(bg, k=2)), extent=(
            CHUNK_SIZE*CHUNK_COORDS[0], 
            CHUNK_SIZE*CHUNK_COORDS[0]+CHUNK_SIZE, 
            CHUNK_SIZE*CHUNK_COORDS[1], 
            CHUNK_SIZE*CHUNK_COORDS[1]+CHUNK_SIZE
            ))
        for swarm in swarms:
            ax.plot(swarm.centro[0], swarm.centro[1], 'ro', label='Centro')
            for entidad in swarm.entidades:
                ax.plot(entidad.posicion[0], entidad.posicion[1], dic_colors[entidad.species], label=entidad.species)

            swarm.mover_entidades(a)
        plt.draw()
        plt.pause(0.04)


def representation(generador, x_range: tuple[int, int], y_range: tuple[int, int]) -> None:
    print(x_range, y_range)
    arr = generador.getChunksInRange(x_range, y_range)
    shape = arr.shape
    color_arr = np.zeros((shape[0], shape[1], 3), dtype=np.uint8)
    biome_names = np.empty((shape[0], shape[1]), dtype=object)
    biome_colors = np.empty((shape[0], shape[1]), dtype=object)

    # Vectorized operations
    unique_biomes = np.unique(arr)
    biome_data = {biome: generator.BIOMAS[biome] for biome in unique_biomes}
        
    for biome, data in biome_data.items():
        mask = arr == biome
        color_arr[mask] = data[2]
        biome_names[mask] = data[1]
        biome_colors[mask] = f"rgb{data[2]}"

    fig = px.imshow(color_arr)
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),  # Set all margins to 0
        showlegend=False,  # Hide the legend
        width=1780,  # Add extra width for the legend
        height=1780  # Add extra height for the legend
    )
    plt.imsave("newplot.png", color_arr)
    return fig

if __name__ == '__main__':
    visualizar_swarms()