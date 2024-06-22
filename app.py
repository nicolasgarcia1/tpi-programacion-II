from jugador import Jugador
from datos import *
from colores import *


print("Menu Principal")
print("1. Jugar")
print("2. Cargar Partida")
print("0. Salir")
opc = int(input("Ingrese una Opcion "))
while opc < 0 or opc > 2:
    opc = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))

salir = True
miPartida = None
while salir:
    if opc == 0:
        salir = False
        print(f"{exito}HASTA LA PROXIMA{reset}")

    elif opc == 1:
        if not miPartida:
            for i, partida in enumerate(partidas):
                print(f"{i+1}. {partida}")
            seleccion = int(input("Ingrese una Partida "))
            while seleccion < 1 or seleccion > len(partidas):
                seleccion = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))
            miPartida = partidas[seleccion-1]

            salida = False
            while not salida:
                nombre = input("Ingrese su Nombre ")
                nombre = nombre.upper()

                for j, color in enumerate(colores):
                    print(f"{j + 1}. {cambiarColor(color)}{color}{reset}")
                seleccion = int(input("Ingrese su Color "))
                while seleccion < 1 or seleccion > len(colores):
                    seleccion = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))
                color = colores[seleccion-1]
                colores.remove(color)

                for j, raza in enumerate(razas):
                    print(f"{j + 1}. {raza}")
                seleccion = int(input("Ingrese su Raza "))
                while seleccion < 1 or seleccion > len(razas):
                    seleccion = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))
                raza = razas[seleccion-1]

                jugador = Jugador(nombre=nombre, color=color, raza=raza)
                miPartida.jugadores = jugador

                if miPartida.cantidadJugadores >= 2 and miPartida.cantidadJugadores < 12:
                    otro = input(f"¿Desea Cargar otro Jugador? ({miPartida.cantidadJugadores}/12) (Y/N) ")
                    otro = otro.lower()
                    while otro != "y" and otro != "n":
                        otro = input(f"{error}Opcion invalida. Ingrese otra{reset} ")
                        otro = otro.lower()
                    if otro == "y":
                        salida = False
                    elif otro == "n":
                        salida = True

        while True:
            for i, jugador in enumerate(miPartida.jugadores):
                print(f"Turno de {cambiarColor(jugador.color)}{jugador.nombre}{reset}")
                PasarTurno = True
                while PasarTurno:
                    print(f"{cambiarColor(jugador.color)}{jugador} Partida: Jugadores({miPartida.cantidadJugadores}){reset}")
                    print("1. Comprar Edificio Madera(500)")
                    print("2. Seleccionar Edificio")
                    print("3. Comprar Unidad")
                    print("4. Seleccionar Unidad")
                    print("5. Pasar Turno")
                    print("0. RENDIRSE")
                    accion = int(input(f"{cambiarColor(jugador.color)}¿Que Desea Hacer?{reset} "))
                    while accion < 0 or accion > 5:
                        accion = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))

                    if accion == 1:
                        if jugador.madera >= 500:
                            jugador.comprarEdificio()
                            print(f"{exito}Edificio Adquirido{reset}")
                        else:
                            print(f"{error}No Posee Suficiente Madera{reset}")
                        
                    elif accion == 2:
                        if len(jugador.edificios) == 0:
                            print(f"{error}No Posee Edificios{reset}")
                        else:
                            for i, edificio in enumerate(jugador.edificios):
                                print(f"{i+1}. {edificio}")
                            seleccion = int(input(f"{cambiarColor(jugador.color)}Seleccione un Edificio{reset} "))
                            while seleccion < 1 or seleccion > len(jugador.edificios):
                                seleccion = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))
                            edificioElegido = jugador.edificios[seleccion-1]
                            print("0. Elimiar Edificio")
                            print("1. Ver Estadisticas")
                            print("2. Mejorar Edificio")
                            opc = int(input(f"{cambiarColor(jugador.color)}¿Que Desea Hacer?{reset} "))
                            while opc < 0 or opc > 2:
                                opc = int(input(f"{error}Opcion invalida, Ingrese otra{reset}: "))

                            if opc == 1:
                                print(edificioElegido)

                            elif opc == 2:
                                if edificioElegido.nivel < 3:
                                    if jugador.oro >= edificioElegido.precioMejoraOro and jugador.madera >= edificioElegido.precioMejoraMadera:                   
                                        jugador.oro = jugador.oro - edificioElegido.precioMejoraOro
                                        jugador.madera = jugador.madera - edificioElegido.precioMejoraMadera
                                        edificioElegido.subirNivel()
                                        print(f"{exito}Edificio Mejorado{reset}")
                                    else:
                                        print(f"{error}No Posee Suficientes Recursos{reset}")
                                else:
                                    print(f"{error}Edificio al Maximo Nivel{reset}")

                            elif opc == 0:
                                jugador.eliminarEdificio(edificioElegido)
                                print(f"{exito}Edificio Eliminado{reset}")

                    elif accion == 3:
                        for i, unidad in enumerate(unidades):
                            print(f"{i+1}. {unidad} precio: {unidad.precioCompra}")
                        seleccion = int(input(f"{cambiarColor(jugador.color)}Que unidad desea comprar{reset} "))
                        while seleccion < 1 or seleccion > len(unidades):
                            seleccion = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))
                        miUnidad = unidades[seleccion-1]
                        if jugador.poblacionActual < jugador.limitePoblacion:
                            if jugador.oro >= miUnidad.precioCompra:
                                jugador.comprarUnidad(miUnidad)
                                print(f"{exito}Unidad Adquirida{reset}")
                            else:
                                print(f"{error}No Posee Suficiente Oro{reset}")
                        else:
                            print(f"{error}No Puede Comprar mas Unidades. Antes debe Ampliar su Reino{reset}")

                    elif accion == 4:
                        if jugador.poblacionActual == 0:
                            print(f"{error}No Posee Unidades{reset}")
                        else:
                            for i, unidad in enumerate(jugador.unidades):
                                print(f"{i+1}. {unidad}")
                            seleccion = int(input(f"{cambiarColor(jugador.color)}Seleccione una unidad{reset} "))
                            while seleccion < 1 or seleccion > jugador.poblacionActual:
                                seleccion = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))
                            unidadElegida = jugador.unidades[seleccion-1]
                            print("0. Elimiar Unidad")
                            print("1. Ver Estadisticas")
                            if unidadElegida.tipoUnidad == "Recolector":
                                print("2. recolectar")
                                opc = int(input(f"{cambiarColor(jugador.color)}¿Que Desea Hacer?{reset} "))
                                while opc < 0 or opc > 2:
                                    opc = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))
                                if opc == 1:
                                    print(unidadElegida)
                                elif opc == 2:
                                    unidadElegida.recolectar()
                                    PasarTurno = False
                                elif opc == 0:
                                    jugador.eliminarUnidad(unidadElegida)
                                    print(f"{exito}Unidad Eliminada{reset}") 
                            else:
                                print("2. Atacar")
                                print("3. Comprar Item")
                                print("4. Vender Item")
                                opc = int(input(f"{cambiarColor(jugador.color)}¿Que Desea Hacer?{reset} "))

                                while opc < 0 or opc > 4:
                                    opc = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))

                                if opc == 1:
                                    print(unidadElegida)

                                elif opc == 2:
                                    unidadElegida.atacar()
                                    PasarTurno = False

                                elif opc == 3:
                                    if len(unidadElegida.mochila) >= 6:
                                        print(f"{error}Esta Unidad tiene la Mochila Llena{reset}")
                                    else:
                                        print("0. Atras")
                                        for i, item in enumerate(items):
                                            print(f"{i+1}. {item}, Precio: {item.precioCompra}")
                                        seleccion = int(input(f"{cambiarColor(jugador.color)}Seleccione el Item a Comprar{reset} "))
                                        while seleccion < 0 or seleccion > len(items):
                                            seleccion = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))
                                        if seleccion != 0:
                                            miItem = items[seleccion-1]
                                            if jugador.oro >= miItem.precioCompra:
                                                unidadElegida.comprarItem(miItem)
                                                jugador.oro = jugador.oro - miItem.precioCompra
                                                print(f"{exito}Item Adquirido{reset}")                                   
                                            else:
                                                print(f"{cambiarColor(jugador.color)}No Posee Suficiente Oro{reset}")
                                
                                elif opc == 4:
                                    if len(unidadElegida.mochila) == 0:
                                        print(f"{error}Esta Unidad no Posee Items en su Mochila{reset}")
                                    else:
                                        print("0. Atras")
                                        for i, item in enumerate(unidadElegida.mochila):
                                            print(f"{i+1}. {item}, Precio: {item.precioVenta}")
                                        seleccion = int(input(f"{cambiarColor(jugador.color)}Seleccione el Item a Vender{reset} "))
                                        while seleccion < 0 or seleccion > len(unidadElegida.mochila):
                                            seleccion = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))
                                        if seleccion != 0:
                                            miItem = unidadElegida.mochila[seleccion-1]
                                            unidadElegida.venderItem(miItem)
                                            jugador.oro = jugador.oro + miItem.precioVenta
                                            print(f"{exito}Item Vendido{reset}")  

                                elif opc == 0:
                                    jugador.eliminarUnidad(unidadElegida)
                                    print(f"{exito}Unidad Eliminada{reset}")

                    elif accion == 5:
                        pasar = input(f"{cambiarColor(jugador.color)}Confirmar Pasar Turno Y/N{reset} ")
                        pasar = pasar.lower()
                        while pasar != "y" and pasar != "n":
                            pasar = input(f"{error}Opcion invalida. Ingrese otra{reset} ")
                            pasar = pasar.lower()
                        if pasar == "y":
                            PasarTurno = False
                        elif pasar == "n":
                            PasarTurno = True
                                
                    elif accion == 0:
                        jugador.perder()
    elif opc == 2:
        miPartida = partidas[0]
        jugador = Jugador(nombre="FACUNDO", color="Rojo", raza="Elfos Oscuros")
        miPartida.jugadores = jugador
        jugador = Jugador(nombre="NICOLAS", color="Verde", raza="Humanos")
        miPartida.jugadores = jugador
        jugador = Jugador(nombre="FRANCISCO", color="Azul", raza="Orcos")
        miPartida.jugadores = jugador
        opc = 1