import random, numpy as np

class Entidad():
    siguiente_id = 1000
    pref = {
        0:25
    }

    def __init__(self, pos_x, pos_y):
        self.id = Entidad.siguiente_id
        self.posicion = (pos_x, pos_y)
        Entidad.siguiente_id += 1


    def move(self):
        r = random.random()
        if (r<0.25): self.pos_x += 1
        elif  (r<0.5): self.pos_x -=1
        elif (r<0.75): self.pos_y +=1
        else: self.pos_y -=1
    
    def moveV3(self, m):
        opciones = np.array(['d', 'u', 'r', 'l'])
        preferencias = self.mvPosiblesV2(m)
        if(preferencias != [0, 0, 0, 0]):
            self.moveAux(random.choices(opciones, preferencias)[0])

    def moveAux(self, dir):
        if(dir == 'd'): self.posicion = (self.posicion[0]+1, self.posicion[1])
        elif(dir == 'u'): self.posicion = (self.posicion[0]-1, self.posicion[1])
        elif(dir == 'r'): self.posicion = (self.posicion[0], self.posicion[1]+1)
        elif(dir == 'l'): self.posicion = (self.posicion[0], self.posicion[1]-1)

    def mvPosiblesV2(self, m):
        obstaculos = np.array([m[self.posicion[0]+1, self.posicion[1]],
                               m[self.posicion[0]-1, self.posicion[1]],
                               m[self.posicion[0], self.posicion[1]+1],
                               m[self.posicion[0], self.posicion[1]-1]])
        preferencias = []
        for e in obstaculos:
            if(Entidad.pref.get(e) is None): 
                preferencias.append(0)
            else: preferencias.append(Entidad.pref.get(e))
        return preferencias
    


    '''def moveV2(self, m):
        opciones = self.mvPosibles(m)
        if(opciones.shape[0] != 0):
            self.moveAux(random.choice(opciones))'''
    
    '''def mvPosibles(self, m):
        obstaculos = np.array([m[self.pos_x+1, self.pos_y], m[self.pos_x-1, self.pos_y], m[self.pos_x, self.pos_y+1], m[self.pos_x, self.pos_y-1]])
        opciones = np.array(['d', 'u', 'r', 'l'])
        filtro = []
        for e in obstaculos:
            if(e != 0): 
                filtro.append(False)
            else: filtro.append(True)
        return opciones[filtro]'''