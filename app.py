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
