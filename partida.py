class Partida():
    def __init__(self, mapa:str, cantidadMadera:int, 
                 cantidadOro:int, cantidadJugadores:int) -> None:
        self.__mapa = mapa
        self.__cantidadMadera = cantidadMadera
        self.__cantidadOro = cantidadOro
        self.__cantidadJugadores = cantidadJugadores

    @property
    def mapa(self) -> str:
        return self.__mapa
    
    @mapa.setter
    def mapa(self, newMapa:str) -> None:
        self.__mapa = newMapa

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
    def cantidadJugadores(self, newCantidadJugadores:int) -> None:
        self.__cantidadJugadores = newCantidadJugadores

    @classmethod
    def empezarPartida(cls) -> None:
        pass

    @classmethod
    def terminarPartida(cls) -> None:
        pass