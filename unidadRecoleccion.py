from unidad import Unidad

class UnidadGuerra(Unidad):
    def __init__(self, tipoUnidad:str, precioCompraOro:int, nivel:int, vida:int, tipoDaño:int, daño:int, tipoDefensa:str, defensa:int, velocidadRecoleccion:int):
        super().__init__(tipoUnidad, precioCompraOro, nivel, vida, tipoDaño, daño)
        self.__velocidadRecoleccion = velocidadRecoleccion
    
    #SETTERS Y GETTERS
    @property
    def velocidadRecoleccion(self):
        return self.__velocidadRecoleccion

    @velocidadRecoleccion.setter
    def velocidadRecoleccion(self, newVelocidadRecoleccion):
        self.__velocidadRecoleccion = newVelocidadRecoleccion
    
    #METODOS
    def recolectar():
        pass #calcular recoleccion