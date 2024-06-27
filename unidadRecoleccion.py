from unidad import Unidad
from colores import neutro, reset

class UnidadRecoleccion(Unidad):
    def __init__(self, tipoUnidad:str="Recolector", precioCompra:int=100, nivel:int=0, vida:int=100, xp:int=0, velocidadRecoleccion:int=100):
        super().__init__(tipoUnidad, precioCompra, nivel, vida, xp)
        self.__velocidadRecoleccion = velocidadRecoleccion
        
    # GETTERS Y SETTERS  
    @property
    def velocidadRecoleccion(self):
        return self.__velocidadRecoleccion
    
    @velocidadRecoleccion.setter
    def velocidadRecoleccion(self, newVelocidadRecoleccion):
        self.__velocidadRecoleccion = newVelocidadRecoleccion
    
    # METODOS
    def recolectar(self):
        self.xp = self.xp + 40
        if self.xp >= 100 and self.nivel < 5:
            self.xp = self.xp - 100
            self.subirNivel()
            self.velocidadRecoleccion = self.velocidadRecoleccion + self.nivel * 10

    
    def __str__(self):
        return f"{self.tipoUnidad} - Vida: {self.vida}, velocidad de Recoleccion: {self.velocidadRecoleccion}, Nivel: {self.nivel}, Precio: {neutro}{self.precioCompra}{reset}"
    