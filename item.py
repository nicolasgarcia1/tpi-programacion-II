from colores import neutro, reset
class Item():
    def __init__(self, nombre:str, precioCompra:int, vida:int, daño:int, defensa:int) -> None:
        self.__nombre = nombre
        self.__precioCompra = precioCompra
        self.__vida = vida
        self.__daño = daño
        self.__defensa = defensa

    # GETTERS Y SETTERS
    @property
    def nombre(self):
        return self.__nombre

    @property
    def precioCompra(self):
        return self.__precioCompra

    @property
    def precioVenta(self):
        return self.__precioCompra - 250

    @property
    def daño(self):
        return self.__daño

    @property
    def vida(self):
        return self.__vida

    @property
    def defensa(self):
        return self.__defensa

    # METODOS
    def __str__(self) -> str:
        return f"{self.nombre} - Vida: {self.vida}, Daño: {self.daño}, Defensa: {self.defensa}, Precio Compra/Venta: {neutro}{self.precioCompra}{reset}/{neutro}{self.precioVenta}{reset}"