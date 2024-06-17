from jugador import Jugador
from edificio import Edificio
from abc import ABC, abstractmethod

# buscar forma de asociar cada unidad creada a su correspondiente jugador
# crear lista de unidades en clase jugador ?

class Unidad(ABC):

    nivel_inicial = 1

    @abstractmethod
    def __init__(self, tipoUnidad:str, precioCompraOro:int,
                 vida:int, tipoDaño:str, daño:int):
        self.__tipoUnidad = tipoUnidad
        self.__precioCompraOro = precioCompraOro
        self.__nivel = Unidad.nivel_inicial
        self.__vida = vida
        self.__tipoDaño = tipoDaño
        self.__daño = daño

    @property
    def tipoUnidad(self):
        return self.__tipoUnidad
    
    @tipoUnidad.setter
    def tipoUnidad(self, newTipoUnidad):
        self.__tipoUnidad = newTipoUnidad

    @property
    def precioCompraOro(self):
        return self.__precioCompraOro
    
    @precioCompraOro.setter
    def precioCompraOro(self, newPrecioCompraOro):
        self.__precioCompraOro = newPrecioCompraOro

    @property
    def nivel(self):
        return self.__nivel
    
    @nivel.setter
    def nivel(self, newNivel):
        self.__nivel = newNivel

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, newVida):
        self.__vida = newVida

    @property
    def tipoDaño(self):
        return self.__tipoDaño
    
    @tipoDaño.setter
    def tipoDaño(self, newTipoDaño):
        self.__tipoDaño = newTipoDaño

    @property
    def daño(self):
        return self.__daño
    
    @daño.setter
    def daño(self, newDaño):
        self.__daño = newDaño

    def morir(self) -> None:
        self.__vida = 0
        print(f"{self.tipoUnidad} ha muerto")
        # crear atributo booleano "muerto" ?