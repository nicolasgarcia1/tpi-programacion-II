from unidad import Unidad
from colores import neutro, reset

class UnidadRecoleccion(Unidad):
    def __init__(self, tipoUnidad:str="Recolector", precioCompra:int=100, nivel:int=1, vida:int=100, xp:int=0, velocidadRecoleccion:int=250):
        super().__init__(tipoUnidad, precioCompra, nivel, vida, xp)
        self.__velocidadRecoleccion = velocidadRecoleccion * self.nivel
        
    # GETTERS Y SETTERS  
    @property
    def velocidadRecoleccion(self):
        return self.__velocidadRecoleccion
    
    @velocidadRecoleccion.setter
    def velocidadRecoleccion(self, newVelocidadRecoleccion):
        self.__velocidadRecoleccion = newVelocidadRecoleccion
    
    # METODOS
    def recolectar():
        pass 
        # al ejecutar este metodo se le pregunta al jugador si quiere oro o madera y resta del atributo de partida 
        # la cantida de madera u oro igual al valor de velocidad de recoleccion de la unidad elegida, por cada vez que un recolector recolecta gana 50 xp

    def __str__(self):
        return f"{self.tipoUnidad} - Vida: {self.vida}, velocidad de Recoleccion: {self.velocidadRecoleccion}, Nivel: {self.nivel}, Precio: {neutro}{self.precioCompra}{reset}"
    