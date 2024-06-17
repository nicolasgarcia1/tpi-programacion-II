from unidadGuerra import UnidadGuerra
# import edificio?

class UnidadMagica(UnidadGuerra):

    mana_inicial = 20

    def __init__(self):
        super().__init__(tipoUnidad='Magica', precioCompraOro=120, vida=50,
                         tipoDaño='hechizo', daño=100)
        self.__mana = UnidadMagica.mana_inicial
        # agregar cantidad de curacion de vida?

    @property
    def mana(self):
        return self.__mana
    
    @mana.setter
    def mana(self, newMana):
        self.__mana = newMana

    def curarUnidad(self):
        pass # pensar como hacer que cure otra unidad

    def revivirUnidad(self):
        pass

    def atacar(self):
        pass