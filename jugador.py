from unidad import Unidad
from edificio import Edificio
class Jugador():
    def __init__(self, nombre:str, color:str, raza:str, oro:int, madera:int) -> None:
        self.__nombre = nombre
        self.__color = color
        self.__raza = raza
        self.__oro = oro
        self.__madera = madera
        self.__unidades = []
        self.__edificios = []
        
    #GETTERS Y SETTERS
    @property
    def nombre(self):
        return self.__nombre
    
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
    def agregarEdificio(self):
        return self.__edificios
    
    @agregarEdificio.setter
    def agregarEdificio(self,nuevo_edificio):
        self.__edificios.append(nuevo_edificio)

    @property
    def agregarUnidad(self):
        return self.__unidades
    
    @agregarUnidad.setter
    def agregarUnidad(self,nueva_unidad):
        self.__unidades.append(nueva_unidad)

    #METODOS
    def comprarEdificio(self, tipoEdificio:str, precioCompraMadera:int,
                 vida:int) -> Edificio :
        nuevo_edificio = Edificio(tipoEdificio, precioCompraMadera, vida)
        self.__edificios.append(nuevo_edificio)
        return nuevo_edificio

    def mejorarEdificios(self, edificio:Edificio):
        if edificio in self.__edificios:
            edificio
        pass

    def eliminarEdificio(self, edificio:Edificio):
        if edificio in self.__edificios:
            self.edificios.remove(edificio)
        pass

    def mejorarUnidades():
        pass

    def eliminarUnidad(self,unidad:Unidad):
        if unidad in self.__unidades:
            self.__unidades.remove(unidad)
        pass

    def perder():
        pass