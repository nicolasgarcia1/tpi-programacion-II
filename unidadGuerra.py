from unidad import Unidad
from item import Item
from colores import neutro, reset

class UnidadGuerra(Unidad):
    def __init__(self, tipoUnidad:str, tipoDaño:str, daño:int, tipoDefensa:str, defensa:int, precioCompra:int, nivel:int=1, vida:int=500, xp:int=0):
        super().__init__(tipoUnidad, precioCompra, nivel, vida, xp)
        self.__tipoDaño = tipoDaño
        self.__daño = daño
        self.__tipoDefensa = tipoDefensa
        self.__defensa = defensa
        self.__mochila = []
    
    # GETTERS Y SETTERS
    @property
    def tipoDaño(self):
        return self.__tipoDaño
    
    @property
    def daño(self):
        return self.__daño
    
    @daño.setter
    def daño(self, newDaño):
        self.__daño = newDaño
    
    @property
    def tipoDefensa(self):
        return self.__tipoDefensa

    @property
    def defensa(self):
        return self.__defensa
    
    @defensa.setter
    def defensa(self, newDefensa):
        self.__defensa = newDefensa
    
    @property
    def mochila(self):
        return self.__mochila
    
    # METODOS
    def atacar(self, unidadAtacada):
        unidadAtacada.vida = unidadAtacada.vida - self.daño
        # selecciona un jugador, selecciona una de sus unidades (puede ser edificio o unidad), se calculan los daños y se actualizan los atributos de los jugadores
        # /se podria hacer un bucle donde las unidades se atacan mutuamente por turnos hasta la muerte de alguno de los dos
        # invocar la/s funcion/es morir de la/s unidad/es correspondiente/s
    
    def comprarItem(self, miItem:Item) -> None:
        self.vida = self.vida + miItem.vida
        self.daño = self.daño + miItem.daño
        self.defensa = self.defensa + miItem.defensa
        self.__mochila.append(miItem)

    def venderItem(self, miItem:Item) -> None:
        self.vida = self.vida - miItem.vida
        self.daño = self.daño - miItem.daño
        self.defensa = self.defensa - miItem.defensa
        self.__mochila.remove(miItem)
        
    def __str__(self):
        return f"{self.tipoUnidad} - Vida: {self.vida}, Ataque: {self.tipoDaño} ({self.daño}), Defensa: {self.tipoDefensa} ({self.defensa}), Nivel: {self.nivel}, Precio: {neutro}{self.precioCompra}{reset}"
