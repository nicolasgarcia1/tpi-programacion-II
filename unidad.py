from abc import ABC


# buscar forma de asociar cada unidad creada a su correspondiente jugador
# crear lista de unidades en clase jugador ?

class Unidad(ABC):

    nivel_inicial = 1

    def __init__(self, tipoUnidad:str, precioCompraOro:int,
                 vida:int, tipoDaño:str, daño:int, jugador):
        self.__tipoUnidad = tipoUnidad
        self.__precioCompraOro = precioCompraOro
        self.__nivel = 1
        self.__vida = vida
        self.__tipoDaño = tipoDaño
        self.__daño = daño
        self.__jugador = jugador

    @property
    def jugador(self):
        return self.__jugador

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

    def morir(self) -> None:
        from jugador import eliminarUnidad
        self.__vida = 0
        print(f"{self.tipoUnidad} ha muerto")
        self.jugador.eliminarUnidad(self)
        # crear atributo booleano "muerto" ?