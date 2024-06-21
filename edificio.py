class Edificio:
    def __init__(self, tipoEdificio:str="Choza", vida: int = 1000, nivel: int = 1) -> None:
        self.__tipoEdificio = tipoEdificio
        self.__vida = vida
        self.__nivel = nivel

    # GETTERS Y SETTERS
    @property
    def tipoEdificio(self) -> int:
        return self.__tipoEdificio

    @tipoEdificio.setter
    def tipoEdificio(self, newTipoEdificio: int) -> None:
        self.__tipoEdificio = newTipoEdificio

    @property
    def vida(self) -> int:
        return self.__vida

    @vida.setter
    def vida(self, newVida) -> None:
        self.__vida = newVida

    @property
    def nivel(self) -> int:
        return self.__nivel

    @nivel.setter
    def nivel(self, newNivel: int) -> None:
        self.__nivel = newNivel

    #CALCULADOS
    @property
    def unidadesPosibles(self):
        if self.nivel == 1:
            return 1
        elif self.nivel == 2:
            return 5
        elif self.nivel == 3:
            return 10
        
    @property
    def precioMejoraOro(self):
        if self.nivel == 1:
            return 500
        elif self.nivel == 2:
            return 1000
        elif self.nivel == 3:
            return "MAX"
        
    @property
    def precioMejoraMadera(self):
        if self.nivel == 1:
            return 500
        elif self.nivel == 2:
            return 1000
        elif self.nivel == 3:
            return "MAX"

    #METODOS
    def subirNivel(self) -> None:
        if self.nivel == 1:
            self.nivel = 2
            self.vida = 1500
            self.nombre = "Hogar"
        elif self.nivel == 2:
            self.nivel = 3
            self.vida = 3000
            self.nombre = "Mansion"

    def __str__(self) -> str:
        return f"Nombre: {self.tipoEdificio}, Vida: {self.vida}, Nivel: {self.nivel}, (+{self.unidadesPosibles} Unidades), mejorar: oro({self.precioMejoraOro}) madera({self.precioMejoraMadera}),"