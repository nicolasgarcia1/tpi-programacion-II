class Jugador():
    def __init__(self, nombre:str, color:str, raza:str, oro:int, madera:int) -> None:
        self.__nombre = nombre
        self.__color = color
        self.__raza = raza
        self.__oro = oro
        self.__madera = madera
        
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

    #METODOS
    def comprarEdificio():
        pass

    def mejorarEdificios():
        pass

    def eliminarEdificio():
        pass

    def mejorarUnidades():
        pass

    def eliminarUnidad():
        pass

    def perder():
        pass