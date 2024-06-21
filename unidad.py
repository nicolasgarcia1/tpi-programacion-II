from abc import ABC, abstractmethod

class Unidad(ABC):
    
    @abstractmethod
    def __init__(self, tipoUnidad:str, precioCompra:int, nivel:int, vida:int, xp:int):
        self.__tipoUnidad = tipoUnidad
        self.__nivel = nivel
        self.__vida = vida
        self.__xp = xp
        self.__precioCompra = precioCompra

    # GETTERS Y SETTERS
    @property
    def tipoUnidad(self):
        return self.__tipoUnidad

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
    def xp(self):
        return self.__xp
    
    @xp.setter
    def xp(self, nueva_xp):
        self.__xp = self.__xp + nueva_xp

    @property
    def precioCompra(self):
        return self.__precioCompra

    #METODOS
    def subirNivel(self):
        # modifica el atributo xp si supera 100 de xp, resta 100 a xp, y asigna el valor con el setter y sube +1 a nivel
        self.__nivel += 1
        self.__xp = 0