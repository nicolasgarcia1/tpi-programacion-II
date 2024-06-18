class Item():
    def __init__(self, nombre:str, precioCompra:int, precioVenta:int, 
                 daño:int, vida:int, defensa:int) -> None:
        self.__nombre = nombre
        self.__precioCompra = precioCompra
        self.__precioVenta = precioVenta
        self.__daño = daño
        self.__vida = vida
        self.__defensa = defensa

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precioCompra(self):
        return self.__precioCompra

    @property
    def precioVenta(self):
        return self.__precioVenta

    @property
    def daño(self):
        return self.__daño

    @property
    def vida(self):
        return self.__vida

    @property
    def defensa(self):
        return self.__defensa

    def __str__(self) -> str:
        attributos = [
            f"Nombre: {self.nombre}",
            f"Precio de Compra: {self.precioCompra}",
            f"Precio de Venta: {self.precioVenta}"
        ]
        if self.daño != 0:
            attributos.append(f"Daño: {self.daño}")
        if self.vida != 0:
            attributos.append(f"Vida: {self.vida}")
        if self.defensa != 0:
            attributos.append(f"defensa: {self.defensa}")
        if self.mana != 0:
            attributos.append(f"Mana: {self.mana}")
        return ', '.join(attributos)