from unidad import Unidad

class UnidadGuerra(Unidad):
    def __init__(self, tipoUnidad:str, precioCompraOro:int, nivel:int, vida:int, tipoDaño:int, daño:int, tipoDefensa:str, defensa:int):
        super().__init__(tipoUnidad, precioCompraOro, nivel, vida, tipoDaño, daño)
        self.__tipoDefensa = tipoDefensa
        self.__defensa = defensa
    
    #SETTERS Y GETTERS
    @property
    def tipoDefensa(self):
        return self.__tipoDefensa

    @property
    def Defensa(self):
        return self.__defensa

    #METODOS
    def atacar():
        pass #calcular ataque