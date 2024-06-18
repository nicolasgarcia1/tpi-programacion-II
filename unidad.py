from abc import ABC, abstractmethod
from jugador import eliminarUnidad
from unidad import Unidad

# buscar forma de asociar cada unidad creada a su correspondiente jugador
# crear lista de unidades en clase jugador ?

class Unidad(ABC):
    
    @abstractmethod
    def __init__(self, tipoUnidad:str, tipoDaño:str, tipoDefensa:str, xp:int, defensa:int=100, daño:int=100, vida:int=500, precioCompraOro:int=100):
        self.__tipoUnidad = tipoUnidad
        self.__nivel = 1
        self.__vida = vida
        self.__tipoDaño = tipoDaño
        self.__tipoDefensa = tipoDefensa
        self.__xp = xp
        # Ajustar el daño según el tipo de daño
        if tipoDaño == "Normal":
            self.__daño = daño
            self.__precioCompraOro = precioCompraOro
        elif tipoDaño == "Perforante":
            self.__daño = daño * 1.25
            self.__precioCompraOro = precioCompraOro * 1.25
        elif tipoDaño == "Asedio":
            self.__daño = daño * 1.50
            self.__precioCompraOro = precioCompraOro * 1.50
        elif tipoDaño == "Magico":
            self.__daño = daño * 1.75
            self.__precioCompraOro = precioCompraOro * 1.75
        
        # Ajustar la defensa según el tipo de defensa
        if tipoDefensa == "Sin Armadura":
            self.__defensa = defensa
            self.__precioCompraOro = self.__precioCompraOro + (precioCompraOro)
        elif tipoDefensa == "Armadura Ligera":
            self.__defensa = defensa * 1.25
            self.__precioCompraOro = self.__precioCompraOro + (precioCompraOro * 1.25)
        elif tipoDefensa == "Armadura Media":
            self.__defensa = defensa * 1.50
            self.__precioCompraOro = self.__precioCompraOro + (precioCompraOro * 1.50)
        elif tipoDefensa == "Armadura Pesada":
            self.__defensa = defensa * 1.75
            self.__precioCompraOro = self.__precioCompraOro + (precioCompraOro * 1.75)

    @property
    def defensa(self):
        return self.__defensa

    @defensa.setter
    def defensa(self,nueva_defensa):
        self.__defensa = nueva_defensa

    @property
    def tipoDefensa(self):
        return self.__tipoDefensa
    
    @tipoDefensa.setter
    def tipoDefensa(self,nuevo_tipoDefensa):
        self.__tipoDefensa = nuevo_tipoDefensa

    @property
    def tipoUnidad(self):
        return self.__tipoUnidad
    
    @tipoUnidad.setter
    def tipoUnidad(self, newTipoUnidad):
        self.__tipoUnidad = newTipoUnidad

    @property
    def precioCompraOro(self):
        return self.__precioCompraOro
    
    @precioCompraOro.setter
    def precioCompraOro(self, newPrecioCompraOro):
        self.__precioCompraOro = newPrecioCompraOro

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
        if self.__vida <= 0:
            self.morir()

    @property
    def tipoDaño(self):
        return self.__tipoDaño
    
    @tipoDaño.setter
    def tipoDaño(self, newTipoDaño):
        self.__tipoDaño = newTipoDaño

    @property
    def daño(self):
        return self.__daño
    
    @daño.setter
    def daño(self, newDaño):
        self.__daño = newDaño

    @property
    def xp(self):
        return self.__xp
    
    @xp.setter
    def xp(self, nueva_xp):
        self.__xp = self.__xp + nueva_xp
        if self.__xp >= 100:
            self.subirnivel(self)

    def morir(self) -> None:
        self.__vida = 0
        self.eliminarUnidad(self)

    def subirnivel(self):
        self.__nivel += 1
        self.__xp = self.__xp - 100