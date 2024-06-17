from datos import *
import os
import platform
import time

def menu_inicial():
    limpiar_pantalla()
    opcion = int(input('''****************MENU DE INICIO****************
    1. Comenzar partida
    2. Editar partida
    3. Cerrar juego
    Seleccione una opcion: '''))
    return opcion

def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    while True:
        opcion = menu_inicial()
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            print('Gracias por jugar GUARCRAF TRE\nCerrando juego...')
            time.sleep(2)
            break
        else:
            print('Opción invalida.')
            time.sleep(1.5)

from jugador import Jugador
from edificio import Edificio
from unidad import Unidad

# Crear jugador
jugador1 = Jugador("Juan", "Rojo", "Humanos", 100, 50)

# Construir un edificio
cuartel = Edificio("Cuartel", 50, 200)

# Crear una unidad desde el edificio, vinculada al jugador propietario
soldado_cuartel = cuartel.crearUnidad("Soldado", 10, 100, "Físico", 20, jugador1)

# Verificar el propietario de la unidad
print(f"El propietario de {soldado_cuartel.tipoUnidad} es {soldado_cuartel.jugador.nombre}")
print(f"Lista de edificios :{jugador1.edificios}")
print(f"Lista de unidades :{jugador1.unidades}")


# Ejemplo de creación y manejo de unidades
from jugador import Jugador
from unidad import Soldado  # Suponiendo que Soldado es una subclase de Unidad

# Crear jugador
jugador1 = Jugador("Juan", "Rojo", "Humano", 100, 50)

# Crear unidad (Soldado)
soldado = Soldado("Soldado", 10, 100, "Físico", 20, jugador1)

# Añadir unidad al jugador
jugador1.unidades.append(soldado)

# Si la unidad muere (vida <= 0), se eliminará automáticamente de la lista de unidades del jugador
soldado.vida = 0  # Esto llamará a soldado.morir() y eliminará soldado de jugador1.unidades
