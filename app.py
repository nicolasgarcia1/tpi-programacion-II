from jugador import Jugador
from edificio import Edificio
from datos import *

print("menu principal")
print("1 jugar")
print("0 salir")
opc = int(input("ingrese una opcion "))
while opc < 0 or opc > 1:
    opc = int(input("opcion invalida, ingrese otra: "))

if opc == 1:
    for i, partida in enumerate(partidas):
        print(f"{i+1}. {partida}")
    seleccion = int(input("Ingrese una partida "))
    while seleccion < 1 or seleccion > len(partidas):
        seleccion = int(input("opcion invalida, ingrese otra: "))
    miPartida = partidas[seleccion-1]
    
    for i in range(miPartida.cantidadJugadores):
        nombre = input("ingrese su nombre ")

        for j, color in enumerate(colores):
            print(f"{j + 1}. {color}")
        seleccion = int(input("ingrese su color "))
        while seleccion < 1 or seleccion > len(colores):
            seleccion = int(input("opcion invalida, ingrese otra: "))
        color = colores[seleccion-1]

        for j, raza in enumerate(razas):
            print(f"{j + 1}. {raza}")
        seleccion = int(input("ingrese su raza "))
        while seleccion < 1 or seleccion > len(razas):
            seleccion = int(input("opcion invalida, ingrese otra: "))
        raza = razas[seleccion-1]

        jugador = Jugador(nombre=nombre, color=color, raza=raza)
        miPartida.jugadores = jugador

    while len(miPartida.jugadores) > 1:
        for i, jugador in enumerate(miPartida.jugadores):
            print("0. rendirse")
            print("1. comprar edificio")
            print("2. seleccionar edificio")
            print("3. comprar unidad")
            print("4. seleccionar unidad")
            print("5. ver stadisticas")
            accion = int(input(f"jugador {i+1} que desea hacer: "))
            while accion < 0 or accion > 6:
                accion = int(input("opcion invalida, ingrese otra: "))

            if accion == 1:
                edificio = Edificio()
                jugador.comprarEdificio(edificio)

            elif accion == 2:
                edificioElegido = jugador.seleccionarEdificio()
                if edificioElegido == 0:
                    print("No tienes edificios disponibles para seleccionar.")
                else:
                    print("0. elimiar edificio")
                    print("1. ver estadisticas")
                    print("2. mejorar edificio")
                    opc = int(input("ingrese una opcion "))
                    while opc < 0 or opc > 2:
                        opc = int(input("Opción invalida, ingrese otra: "))

                    if opc == 1:
                        print(edificioElegido)

                    elif opc == 2:
                        if edificioElegido.nivel < 3:
                            if jugador.oro >= edificioElegido.precioMejoraOro and jugador.madera >= edificioElegido.precioMejoraMadera:                   
                                jugador.oro = jugador.oro - edificioElegido.precioMejoraOro
                                jugador.madera = jugador.madera - edificioElegido.precioMejoraMadera
                                edificioElegido.subirNivel()
                            else:
                                print("no posee suficiente oro o madera")
                        else:
                            print("edificio mejorado al maximo")

                    elif opc == 0:
                        jugador.eliminarEdificio(edificioElegido)

            elif accion == 3:
                for i, unidad in enumerate(unidades):
                    print(f"{i+1}. {unidad} precio: {unidad.precioCompra}")
                seleccion = int(input("Que unidad desea comprar "))
                while seleccion < 1 or seleccion > len(unidades):
                    seleccion = int(input("opcion invalida, ingrese otra: "))
                miUnidad = unidades[seleccion-1]
                jugador.comprarUnidad(miUnidad)

            elif accion == 4:
                unidadElegida = jugador.seleccionarUnidad()
                if unidadElegida == 0:
                    print("No tienes unidades disponibles para seleccionar.")
                else:
                    print("0. elimiar unidad")
                    print("1. ver estadisticas")
                    if unidadElegida.tipoUnidad == "Recolector":
                        print("2. recolectar")
                        opc = int(input("ingrese una opcion "))
                        while opc < 0 or opc > 2:
                            opc = int(input("Opción invalida, ingrese otra: "))
                        if opc == 1:
                            print(unidadElegida)
                        elif opc == 2:
                            unidadElegida.recolectar()
                        elif opc == 0:
                            jugador.eliminarUnidad(unidadElegida)    
                    else:
                        print("2. atacar")
                        print("3. comprar item")
                        print("4. vender item")
                        opc = int(input("ingrese una opcion "))
                        while opc < 0 or opc > 4:
                            opc = int(input("Opción invalida, ingrese otra: "))
                        if opc == 1:
                            print(unidadElegida)
                        elif opc == 2:
                            unidadElegida.atacar()
                        elif opc == 3:
                            
                            if len(unidadElegida.mochila) >= 6:
                                print("no puede comprar mas de 6 items por unidad")
                            else:
                                for i, item in enumerate(items):
                                    print(f"{i+1}. {item}, precio: {item.precioCompra}")
                                seleccion = int(input("que item desea comprar "))
                                while seleccion < 1 or seleccion > len(items):
                                    seleccion = int(input("opcion invalida, ingrese otra: "))
                                miItem = items[seleccion-1]
                                if jugador.oro >= miItem.precioCompra:
                                    unidadElegida.comprarItem(miItem)
                                    jugador.oro = jugador.oro - miItem.precioCompra                                    
                                else:
                                    print("no posee suficiente oro para comprar el item")
                        
                        elif opc == 4:
                            if len(unidadElegida.mochila) == 0:
                                print("esta unidad no posee items en su mochila")
                            else:
                                for i, item in enumerate(unidadElegida.mochila):
                                    print(f"{i+1}. {item}, precio: {item.precioVenta}")
                                seleccion = int(input("que item desea vender "))
                                while seleccion < 1 or seleccion > len(unidadElegida.mochila):
                                    seleccion = int(input("opcion invalida, ingrese otra: "))
                                miItem = unidadElegida.mochila[seleccion-1]
                                unidadElegida.venderItem(miItem)
                                jugador.oro = jugador.oro + miItem.precioVenta 
                        elif opc == 0:
                            jugador.eliminarUnidad(unidadElegida)

            elif accion == 5:
                print(jugador)

            elif accion == 0:
                jugador.perder()
elif opc == 0:
    print("adios")