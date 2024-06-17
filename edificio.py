from jugador import Jugador

class Edificio():
    def __init__(self, tipoEdificio:str, precioCompraMadera:int,
                 vida:int) -> None:
        self.__tipoEdificio = tipoEdificio
        self.__precioCompraMadera = precioCompraMadera
        self.__vida = vida

    @property
    def tipoEdificio(self):
        return self.__tipoEdificio
    
    @tipoEdificio.setter
    def tipoEdificio(self, newTipoEdificio:str):
        self.__tipoEdificio = newTipoEdificio

    @property
    def precioCompraMadera(self):
        return self.__precioCompraMadera
    
    @precioCompraMadera.setter
    def precioCompraMadera(self, newPrecioCompraMadera:int):
        self.__precioCompraMadera = newPrecioCompraMadera

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, newVida:int):
        self.__vida = newVida

    def crearUnidad():
        pass

    def morir():
        pass