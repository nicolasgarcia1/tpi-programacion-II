from unidad import Unidad

class UnidadRecoleccion(Unidad):
    def __init__(self, tipoUnidad:str, precioCompraOro:int,xp:int, nivel:int, vida:int, tipoDaño:int, daño:int, velocidadRecoleccion:int):
        super().__init__(tipoUnidad, precioCompraOro,xp , nivel, vida, tipoDaño, daño)
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