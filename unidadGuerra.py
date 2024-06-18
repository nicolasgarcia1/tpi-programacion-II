from unidad import Unidad
from item import Item

class UnidadGuerra(Unidad):
    def __init__(self, tipoUnidad:str, precioCompraOro:int, nivel:int, vida:int, tipoDaño:int, daño:int, tipoDefensa:str, defensa:int):
        super().__init__(tipoUnidad, precioCompraOro, nivel, vida, tipoDaño, daño)
        self.__tipoDefensa = tipoDefensa
        self.__defensa = defensa
        self.__mochila = []
    
    #SETTERS Y GETTERS
    @property
    def tipoDefensa(self):
        return self.__tipoDefensa

    @property
    def Defensa(self):
        return self.__defensa

    @property
    def mochila(self):
        return self.__mochila

    @mochila.setter
    def mochila(self,nueva_mochila:list):
        self.__mochila = nueva_mochila
        

    #METODOS
    def atacar():
        pass #calcular ataque
    
    def comprar_item(self, item:Item) -> None:
        if len(self.__mochila) >= 6 or item in self.__mochila:
            raise Exception # ?? ver como hacer
        else:
            self.__mochila.append(item)

    def vender_item(self, item:Item) -> None:
        if len(self.__mochila) == 0 or item not in self.__mochila:
            raise Exception 
        else:
            self.__mochila.remove(item)