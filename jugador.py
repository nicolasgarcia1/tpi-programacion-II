from unidad import Unidad
from edificio import Edificio

class Jugador():
    def __init__(self, nombre:str, color:str, raza:str, oro:int, madera:int, edificios:int=0) -> None:
        self.__nombre = nombre
        self.__color = color
        self.__raza = raza
        self.__oro = oro
        self.__madera = madera
        self.__unidades = []
        self.__edificios = edificios
        
    #GETTERS Y SETTERS
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter

    
    @property
    def color(self):
        return self.__color
    
    @property
    def raza(self):
        return self.__raza
        
    @property
    def oro(self):
        return self.__oro

    @oro.setter
    def oro(self, newOro):
        self.__oro = newOro
    
    @property
    def madera(self):
        return self.__madera

    @madera.setter
    def madera(self, newMadera):
        self.__madera = newMadera

    @property
    def limitePoblacion():
        pass #calcular el limite de poblacion

    @property
    def poblacionActual():
        pass #calcular poblacion actual

    @property
    def edificios(self):
        return self.__edificios
    
    @edificios.setter
    def edificios(self, newEdificio):
        self.__edificios = newEdificio
    
    @property
    def unidades(self):
        return self.__unidades
    
    @unidades.setter
    def agregarUnidad(self, nuevas_unidades):
        self.__unidades = nuevas_unidades

    #METODOS

    def comprarUnidad(self, tipoUnidad, tipoDaño, tipoDefensa, xp, defensa, daño, vida, precioCompraOro):
        nueva_unidad = Unidad(tipoUnidad, tipoDaño, tipoDefensa, xp, defensa, daño, vida, precioCompraOro)
        self.__unidades.append(nueva_unidad)
    def comprarEdificio(self, precioCompraMadera:int,
                 vida:int) -> Edificio :
        if self.__madera >= 15:
            nuevo_edificio = Edificio(precioCompraMadera, vida)
            self.__edificios += 1
            return nuevo_edificio
        pass

    def eliminarEdificio(self):
        self.__edificios -= 1
        pass

    
    def crearUnidad(self, tipoUnidad:str, precioCompraOro:int,
                 vida:int, tipoDaño:str, daño:int, jugador:str):
        nueva_unidad = Unidad(tipoUnidad, precioCompraOro, vida, tipoDaño, daño)
        self.agregarUnidad(self, nueva_unidad)
        return nueva_unidad


    def eliminarUnidad(self, unidad:Unidad):
        if unidad in self.__unidades:
            self.__unidades.remove(unidad)
        pass

    def perder():
        pass