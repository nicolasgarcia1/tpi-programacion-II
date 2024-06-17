from unidad import Unidad
class Edificio():
    def __init__(self, tipoEdificio:str, precioCompraMadera:int,
                 vida:int) -> None:
        self.__tipoEdificio = tipoEdificio
        self.__precioCompraMadera = precioCompraMadera
        self.__vida = vida

    @property
    def tipoEdificio(self):
        return self.__tipoEdificio
    
    @tipoEdificio.setter
    def tipoEdificio(self, newTipoEdificio:str):
        self.__tipoEdificio = newTipoEdificio

    @property
    def precioCompraMadera(self):
        return self.__precioCompraMadera
    
    @precioCompraMadera.setter
    def precioCompraMadera(self, newPrecioCompraMadera:int):
        self.__precioCompraMadera = newPrecioCompraMadera

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, newVida:int):
        self.__vida = newVida
        if self.__vida <= 0:
            self.morir()

    def crearUnidad(self, tipoUnidad:str, precioCompraOro:int,
                 vida:int, tipoDaño:str, daño:int, jugador:str):
        nueva_unidad = Unidad(tipoUnidad, precioCompraOro, vida, tipoDaño, daño , jugador)
        return nueva_unidad

    def morir(self):
        self.__vida = 0
        print(f"{self.tipoEdificio} ha muerto")
        del self