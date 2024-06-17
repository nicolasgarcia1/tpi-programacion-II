from unidadGuerra import UnidadGuerra
from item import Item

class UnidadHeroe(UnidadGuerra):

    experiencia_inicial = 1

    def __init__(self):
        super().__init__(tipoUnidad='Heroe', precioCompraOro=100, 
                         vida=150, tipoDaño='melee', daño=75, 
                         tipoDefensa='?', defensa=100)
        self.__experiencia = UnidadHeroe.experiencia_inicial
        self.__mochila = []

    @property
    def experiencia(self):
        return self.__experiencia
    
    @experiencia.setter
    def experiencia(self, newExperiencia):
        self.__experiencia = newExperiencia

    def atacar(self):
        pass

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