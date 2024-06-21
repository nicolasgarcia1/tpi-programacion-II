from jugador import Jugador

class Partida():
    def __init__(self, mapa:str, cantidadMadera:int, cantidadOro:int, cantidadJugadores:int) -> None:
        self.__mapa = mapa
        self.__cantidadMadera = cantidadMadera
        self.__cantidadOro = cantidadOro
        self.__cantidadJugadores = cantidadJugadores
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
    def cantidadJugadores(self) -> int:
        return self.__cantidadJugadores
    
    @cantidadJugadores.setter
    def cantidadJugadores(self, NewCantidadJugadores):
        self.__cantidadJugadores = NewCantidadJugadores

    @property
    def jugadores(self):
        return self.__jugadores
    
    @jugadores.setter
    def jugadores(self, jugador:Jugador):
        self.__jugadores.append(jugador)
    
    # METODOS
    def terminarPartida(self) -> None:
        pass
        # se llama desde el metodo perder de jugador y valida si la cantidad de jugadores en la lista de jugadores 
        # es igual a 1 y en caso positivo lo declara ganador y finaliza la ejecucion del codigo

    def __str__(self):
        return (f"Mapa: {self.mapa}, Cantidad de Madera: {self.cantidadMadera}, Cantidad de Oro: {self.cantidadOro}, Cantidad de Jugadores: {self.cantidadJugadores}")
