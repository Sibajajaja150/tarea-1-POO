#Esteban Sibaja 202036965
import random

class Dado:
    caras=6
    
    def __init__(self, numCaras):
        self.caras=numCaras
    
    def tiro(self):
        return random.randint(1, self.caras)
