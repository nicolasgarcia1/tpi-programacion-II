from abc import ABC, abstractmethod

class Unidad(ABC):
    
    @abstractmethod
    def __init__(self, tipoUnidad:str, precioCompra:int, nivel:int, vida:int, xp:int):
        self._tipoUnidad = tipoUnidad
        self._nivel = nivel
        self._vida = vida
        self._xp = xp
        self._precioCompra = precioCompra

    # GETTERS Y SETTERS
    @property
    def tipoUnidad(self):
        return self._tipoUnidad

    @property
    def nivel(self):
        return self._nivel
    
    @nivel.setter
    def nivel(self, newNivel):
        self._nivel = newNivel

    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, newVida):
        self._vida = newVida

    @property
    def xp(self):
        return self._xp
    
    @xp.setter
    def xp(self, nueva_xp):
        self._xp = nueva_xp

    @property
    def precioCompra(self):
        return self._precioCompra

    #METODOS
    def subirNivel(self):
            self.nivel = self.nivel + 1
