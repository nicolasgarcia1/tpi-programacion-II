from jugador import Jugador
from colores import neutro, reset

class Partida():
    def __init__(self, mapa:str, cantidadMadera:int, cantidadOro:int) -> None:
        self.__mapa = mapa
        self.__cantidadMadera = cantidadMadera
        self.__cantidadOro = cantidadOro
        self.__jugadores = []

    # GETTERS Y SETTERS
    @property
    def mapa(self) -> str:
        return self.__mapa

    @property
    def cantidadMadera(self) -> int:
        return self.__cantidadMadera
    
    @cantidadMadera.setter
    def cantidadMadera(self, newCantidadMadera:int) -> None:
        self.__cantidadMadera = newCantidadMadera

    @property
    def cantidadOro(self) -> int:
        return self.__cantidadOro
    
    @cantidadOro.setter
    def cantidadOro(self, newCantidadOro:int) -> None:
        self.__cantidadOro = newCantidadOro

    @property
    def jugadores(self):
        return self.__jugadores
    
    @jugadores.setter
    def jugadores(self, jugador:Jugador):
        self.__jugadores.append(jugador)
    
    # CALCULADOS
    @property
    def cantidadJugadores(self) -> int:
        return len(self.__jugadores)
    
    # METODOS
    def terminarPartida(self) -> None:
        if self.cantidadJugadores == 1:
            return True
        else:
            return False
        # se llama desde el metodo perder de jugador y valida si la cantidad de jugadores en la lista de jugadores 
        # es igual a 1 y en caso positivo lo declara ganador y finaliza la ejecucion del codigo

    def __str__(self):
        return (f"Mapa: {self.mapa}, Oro: {neutro}{self.cantidadOro}{reset} , Madera: {neutro}{self.cantidadMadera}{reset}")
