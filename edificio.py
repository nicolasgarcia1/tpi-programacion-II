from unidad import Unidad
from jugador import eliminarEdificio

class Edificio():
    def __init__(self, precioCompraMadera:int,
                 vida:int) -> None:
        self.__precioCompraMadera = precioCompraMadera
        self.__vida = vida

    
    @property
    def precioCompraMadera(self):
        return self.__precioCompraMadera
    
    @precioCompraMadera.setter
    def precioCompraMadera(self, nuevo_precioCompraMadera):
        self.__precioCompraMadera = nuevo_precioCompraMadera
    

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, newVida:int):
        self.__vida = newVida
        if self.__vida <= 0:
            self.morir()

    def morir(self):
        self.__vida = 0
        self.eliminarEdificio(self)
        del self