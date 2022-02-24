#Esteban Sibaja 2020036965
from Ficha import *

class Tablero: #clase principal
    Name = ""
    Players = []
    dice = None 
    NumSpaces = 0
    NumPlayers = 0
 
    def __init__(self, Name, NumSpaces): #metodo constructor
        self.Name = Name
        self.Players = [Ficha("Azul", "Azul"), Ficha("Rojo", "Rojo")]
        self.NumSpaces = NumSpaces
        self.dice = Dado(6)
        self.NumPlayers  = 5

    def turn(self): #metodo para los turnos
        self.Players[0].avanzar()
        if self.Players[0].posicion >= self.espacios: 
            print("Gano:", self.Players[0].color)
            return True 
        else: 
            self.Players.append(self.jPlayers.pop(0))
            return False 

    def juego(self): #metodo para inicar el juego
        play = True
        while(play): 
            res = self.turn()
            if(res): 
                play = False

tablero = Tablero("Juego", 30)
tablero.juego()