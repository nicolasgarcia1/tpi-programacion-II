from unidad import Unidad
from edificio import Edificio

class Jugador():
    __listaNombres = []
    __listaColores = []

    def __init__(self, nombre:str, color:str, raza:str, oro:int=5000, madera:int=5000) -> None:
        self.__nombre = Jugador.__validarNombre(nombre)
        self.__color = Jugador.__validarColor(color)
        self.__raza = raza
        self.__oro = oro
        self.__madera = madera
        self.__edificios = []
        self.__unidades = []

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
                limitePoblacion = limitePoblacion +10
        return limitePoblacion

    @property
    def poblacionActual(self):
        return len(self.__unidades)

    # METODOS
    @classmethod
    def __validarNombre(cls, nombre):
        if nombre in Jugador.__listaNombres:
            raise Exception("Error: nombre ya utilizado")
        Jugador.__listaNombres.append(nombre)
        return nombre

    @classmethod
    def __validarColor(cls, color):
        if color in Jugador.__listaColores:
            raise Exception("Error: color ya utilizado")
        Jugador.__listaColores.append(color)
        return color

    def comprarEdificio(self, edificio:Edificio):
        if self.madera >= 500:
            self.__edificios.append(edificio)
            self.madera = self.madera - 500
        else:
            print("no posee suficiente madera para realizar la compra")

    def seleccionarEdificio(self):
        if len(self.edificios) == 0:
            return 0
        else:
            for i, edificio in enumerate(self.edificios):
                print(f"{i+1}. {edificio}")
            seleccion = int(input("Seleccione una edificio "))
            while seleccion < 1 or seleccion > len(self.edificios):
                seleccion = int(input("opcion invalida, ingrese otra: "))
            edificioElegido = self.edificios[seleccion-1]
            return edificioElegido
        
    def eliminarEdificio(self, edificioElegido:Edificio):
        self.__edificios.remove(edificioElegido)

    def comprarUnidad(self, miUnidad:Unidad):
        if self.poblacionActual < self.limitePoblacion:
            if self.oro >= miUnidad.precioCompra:
                self.__unidades.append(miUnidad)
                newOro = self.oro - miUnidad.precioCompra
                self.oro = newOro
            else:
                print("No tienes suficiente oro para comprar esta unidad")
        else:
            print("no puede comprar mas unidades antes debe ampliar su reino")

    def seleccionarUnidad(self):
        if len(self.unidades) == 0:
            return 0
        else:
            for i, unidad in enumerate(self.unidades):
                print(f"{i+1}. {unidad}")
            seleccion = int(input("Seleccione una unidad "))
            while seleccion < 1 or seleccion > len(self.unidades):
                seleccion = int(input("opcion invalida, ingrese otra: "))
            unidadElegida = self.unidades[seleccion-1]
            return unidadElegida

    def eliminarUnidad(self, unidadElegida):
        self.__unidades.remove(unidadElegida)

    def perder(self):
        pass
        # cuando una unidad muera verificar si fue la ultima del jugador en caso positivo remover al jugador de la lista de jugadores 
        # y en ese mismo paso invocar el metodo terminarPartida el cual validara si la cantidad de jugadores en la lista de jugadores 
        # es igual a 1 y en caso positivo lo declara ganador y finaliza la ejecucion del codigo

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Color: {self.color}\n"
                f"Raza: {self.raza}\n"
                f"Oro: {self.oro}\n"
                f"Madera: {self.madera}\n"
                f"Edificios: {len(self.edificios)}\n"
                f"Limite de Poblacion: {self.limitePoblacion}\n"
                f"Poblacion Actual: {len(self.unidades)}")