#Esteban sibaja 2020036965
from Dado import *

class Ficha: #clase para la ficha
    color = " "
    pos = 0
    name = " "
    dado = Dado(6)
    
    def __init__(self, color, name): #metodo constructor
        self.color = color
        self.pos = 0
        self.name = name 
    
    def avanzar(self): #metodo que permite avanzar
        steps = self.dado.tiro()
        self.pos += steps
        print(self.color, " tiró ",  steps)
        print("jugador:", self.color, "esta en la posicion",self.pos)