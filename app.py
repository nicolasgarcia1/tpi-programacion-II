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
