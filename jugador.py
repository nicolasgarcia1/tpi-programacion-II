from unidad import Unidad
from unidadRecoleccion import UnidadRecoleccion
from edificio import Edificio
from colores import *
import copy

class Jugador():
    __listaNombres = []
    __listaColores = []

    def __init__(self, nombre:str, color:str, raza:str, oro:int=0, madera:int=0) -> None:
        self.__nombre = Jugador.__validarNombre(nombre)
        self.__color = Jugador.__validarColor(color)
        self.__raza = raza
        self.__oro = oro
        self.__madera = madera
        self.__edificios = [Edificio()]
        self.__unidades = [UnidadRecoleccion()]

    # GETTERS Y SETTERS
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
    def edificios(self):
        return self.__edificios

    @property
    def unidades(self):
        return self.__unidades

    # CALCULADOS
    @property
    def limitePoblacion(self):
        limitePoblacion = 0
        for edificio in self.edificios:
            if edificio.nivel == 1:
                limitePoblacion = limitePoblacion + 1
            elif edificio.nivel == 2:
                limitePoblacion = limitePoblacion + 5
            elif edificio.nivel == 3:
                limitePoblacion = limitePoblacion + 10
        return limitePoblacion

    @property
    def poblacionActual(self):
        return len(self.unidades)
    
    @property
    def cantEdificios(self):
        return len(self.edificios)

    # METODOS
    @classmethod
    def __validarNombre(cls, nombre):
        if nombre in Jugador.__listaNombres:
            raise Exception(f"{error}Error: Nombre ya Utilizado{reset}")
        Jugador.__listaNombres.append(nombre)
        return nombre

    @classmethod
    def __validarColor(cls, color):
        if color in Jugador.__listaColores:
            raise Exception(f"{error}Error: Color ya Utilizado{reset}")
        Jugador.__listaColores.append(color)
        return color

    def comprarEdificio(self):
        edificio = Edificio()
        self.__edificios.append(edificio)
        self.madera = self.madera - 500
        
    def eliminarEdificio(self, edificioElegido:Edificio):
        self.__edificios.remove(edificioElegido)

    def comprarUnidad(self, miUnidad:Unidad):
        miUnidad = copy.deepcopy(miUnidad)
        self.__unidades.append(miUnidad)
        newOro = self.oro - miUnidad.precioCompra
        self.oro = newOro

    def eliminarUnidad(self, unidadElegida):
        self.__unidades.remove(unidadElegida)
       
    def perder(self):
        pass
        # cuando una unidad muera verificar si fue la ultima del jugador en caso positivo remover al jugador de la lista de jugadores 
        # y en ese mismo paso invocar el metodo terminarPartida el cual validara si la cantidad de jugadores en la lista de jugadores 
        # es igual a 1 y en caso positivo lo declara ganador y finaliza la ejecucion del codigo

    def __str__(self):
        return f"{self.nombre}: Oro({neutro}{self.oro}{cambiarColor(self.color)}), Madera({neutro}{self.madera}{cambiarColor(self.color)}), {self.raza}({self.poblacionActual}/{self.limitePoblacion}), Edificios({len(self.edificios)})"