class Item():
    def __init__(self, nombre:str, precioCompra:int, precioVenta:int, daño:int, vida:int, armadura:int, mana,int) -> None:
        self.__nombre = nombre
        self.__precioCompra = precioCompra
        self.__precioVenta = precioVenta
        self.__daño = daño
        self.__vida = vida
        self.__armadura = armadura
        self.__mana = mana

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
    def armadura(self):
        return self.__armadura

    @property
    def mana(self):
        return self.__mana

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
        if self.armadura != 0:
            attributos.append(f"Armadura: {self.armadura}")
        if self.mana != 0:
            attributos.append(f"Mana: {self.mana}")
        return ', '.join(attributos)