from jugador import Jugador
from datos import *
from colores import *
import time

def seleccionar(lista:list, color:str=None):
    for i, elemento in enumerate(lista):
        if elemento in colores:
            print(f"{i+1}. {cambiarColor(elemento)}{elemento}{reset}")
        else:
            print(f"{i+1}. {elemento}")

    if color:
        seleccion = int(input(f"{cambiarColor(color)}Ingrese una Opcion{reset} "))
    else:
        seleccion = int(input(f"{neutro}ingrese una Opcion{reset} "))
    
    while seleccion < 1 or seleccion > len(lista):
        seleccion = int(input(f"{error}Opcion invalida. Ingrese otra{reset} "))
    return seleccion

def siono(respuesta):
    respuesta = respuesta.lower()
    while respuesta != "y" and respuesta != "n":
        respuesta = input(f"{error}Opcion invalida. Ingrese otra{reset} ")
        respuesta = respuesta.lower()

    if respuesta == "y":
        return True
    elif respuesta == "n":
        return False
    
def limpiarPantalla():
    print("\033c", end="")

def printar(mensaje:str):
    limpiarPantalla()
    print(mensaje)
    time.sleep(1)


salir = False
while not salir:
    limpiarPantalla()
    print("Menu Principal")
    menu = ["Jugar",
            "Cargar Partida",
            "Salir"]
    opc = seleccionar(menu)

    if opc == 1 or opc == 2:
        if opc == 1:
            limpiarPantalla()
            miPartida = partidas[seleccionar(partidas)-1]

            empezar = False
            while not empezar:
                limpiarPantalla()
                nombre = input(f"{neutro}Jugaddor {miPartida.cantidadJugadores + 1} Ingrese su Nombre{reset} ")
                nombre = nombre.upper()

                limpiarPantalla()
                color = colores[seleccionar(colores)-1]
                colores.remove(color)

                limpiarPantalla()
                raza = razas[seleccionar(razas)-1]

                jugador = Jugador(nombre, color, raza)
                miPartida.jugadores = jugador
                
                if miPartida.cantidadJugadores >= 2 and miPartida.cantidadJugadores < 12:
                    limpiarPantalla()
                    empezar = input(f"{neutro}¿Empezar Partida? Jugadores ({miPartida.cantidadJugadores}/12) (Y/N){reset} ")
                    empezar = siono(empezar)

        elif opc == 2:
            miPartida = partidas[1-1]
            jugador = Jugador("FACUNDO","Rojo","Elfos Oscuros")
            miPartida.jugadores = jugador
            jugador = Jugador("NICOLAS","Verde","Humanos")
            miPartida.jugadores = jugador
            jugador = Jugador("FRANCISCO","Amarillo","Orcos")
            miPartida.jugadores = jugador

        jugadoresTotales = miPartida.cantidadJugadores
        while True:
            for jugador in miPartida.jugadores:
                printar(f"Turno de {cambiarColor(jugador.color)}{jugador.nombre}{reset}")
                pasar = False
                while not pasar:
                    limpiarPantalla()
                    print(f"{cambiarColor(jugador.color)}{jugador}{reset} // {neutro}Partida: Jugadores({miPartida.cantidadJugadores}/{jugadoresTotales}){reset}")
                    menu = [f"Comprar Edificio por {neutro}500{reset} de Madera",
                            "Comprar Unidad",
                            "Seleccionar Edificio",
                            "Seleccionar Unidad",
                            "Pasar Turno",
                            "RENDIRSE"]
                    opc = seleccionar(menu, jugador.color)

                    if opc == 1:
                        if jugador.madera >= 500:
                            jugador.comprarEdificio()
                            printar(f"{exito}Edificio Adquirido{reset}")
                        else:
                            printar(f"{error}No Posee Suficiente Madera{reset}")

                    elif opc == 2:
                        limpiarPantalla()
                        miUnidad = unidades[seleccionar(unidades, jugador.color)-1]
                        if jugador.poblacionActual < jugador.limitePoblacion:
                            if jugador.oro >= miUnidad.precioCompra:
                                jugador.comprarUnidad(miUnidad)
                                printar(f"{exito}Unidad Adquirida{reset}")
                            else:
                                printar(f"{error}No Posee Suficiente Oro{reset}")
                        else:
                            printar(f"{error}No Puede Comprar mas Unidades. Antes debe Ampliar su Reino{reset}")

                    elif opc == 3:
                        if len(jugador.edificios) == 0:
                            printar(f"{error}No Posee Edificios{reset}")
                        else:
                            limpiarPantalla()
                            edificioElegido = jugador.edificios[seleccionar(jugador.edificios, jugador.color)-1]
                            limpiarPantalla()
                            print(edificioElegido)
                            menu = ["Mejorar",
                                    "Elimiar"]
                            opc = seleccionar(menu, jugador.color)

                            if opc == 1:
                                if edificioElegido.nivel < 3:
                                    if jugador.oro >= edificioElegido.precioMejoraOro and jugador.madera >= edificioElegido.precioMejoraMadera:                   
                                        jugador.oro = jugador.oro - edificioElegido.precioMejoraOro
                                        jugador.madera = jugador.madera - edificioElegido.precioMejoraMadera
                                        edificioElegido.subirNivel()
                                        printar(f"{exito}Edificio Mejorado{reset}")
                                    else:
                                        printar(f"{error}No Posee Suficientes Recursos{reset}")
                                else:
                                    printar(f"{error}Edificio Mejorado al Maximo{reset}")

                            elif opc == 2:
                                if jugador.cantEdificios == 1:
                                    printar(f"{error}No Puede Eliminar Todos sus Edificios{reset}")
                                else:
                                    jugador.eliminarEdificio(edificioElegido)
                                    printar(f"{exito}Edificio Eliminado{reset}")

                    elif opc == 4:
                        if jugador.poblacionActual == 0:
                            printar(f"{error}No Posee Unidades{reset}")
                        else:
                            limpiarPantalla()
                            unidadElegida = jugador.unidades[seleccionar(jugador.unidades, jugador.color)-1]
                            if isinstance(unidadElegida, UnidadRecoleccion):
                                limpiarPantalla()
                                print(unidadElegida)
                                menu = ["Recolectar",
                                        "Elimiar"]
                                opc = seleccionar(menu, jugador.color)

                                if opc == 1:# FALTA IMPLEMENTAR ##############################################################################
                                    unidadElegida.recolectar
                                    PasarTurno = False
                                
                                elif opc == 2:
                                    cantRecoleccion = sum(1 for unidad in jugador.unidades if isinstance(unidad, UnidadRecoleccion))
                                    if cantRecoleccion == 1:
                                        printar(f"{error}No Puede Eliminar Todas sus Unidades de Recoleccion{reset}")
                                    else:
                                        jugador.eliminarUnidad(unidadElegida)
                                        printar(f"{exito}Unidad Eliminada{reset}") 

                            else:
                                limpiarPantalla()
                                print(unidadElegida)
                                menu = ["Atacar",
                                        "Comprar Item",
                                        "Vender Item",
                                        "Elimiar"]
                                opc = seleccionar(menu, jugador.color)

                                if opc == 1:# FALTA IMPLEMENTAR ##############################################################################
                                    unidadElegida.atacar
                                    PasarTurno = False
                                
                                elif opc == 2:
                                    if len(unidadElegida.mochila) >= 6:
                                        printar(f"{error}Esta Unidad tiene la Mochila Llena{reset}")
                                    else:
                                        limpiarPantalla()
                                        miItem = items[seleccionar(items, jugador.color)-1]
                                        if jugador.oro >= miItem.precioCompra:
                                            unidadElegida.comprarItem(miItem)
                                            jugador.oro = jugador.oro - miItem.precioCompra
                                            printar(f"{exito}Item Adquirido{reset}")                                   
                                        else:
                                            printar(f"{error}No Posee Suficiente Oro{reset}")
                                
                                elif opc == 3:
                                    if len(unidadElegida.mochila) == 0:
                                        printar(f"{error}Esta Unidad no Posee Items en su Mochila{reset}")
                                    else:
                                        limpiarPantalla()
                                        miItem = unidadElegida.mochila[seleccionar(unidadElegida.mochila, jugador.color)-1]
                                        unidadElegida.venderItem(miItem)
                                        jugador.oro = jugador.oro + miItem.precioVenta
                                        printar(f"{exito}Item Vendido{reset}")

                                elif opc == 4:
                                    jugador.eliminarUnidad(unidadElegida)
                                    printar(f"{exito}Unidad Eliminada{reset}")

                    elif opc == 5:
                        limpiarPantalla()
                        pasar = input(f"{cambiarColor(jugador.color)}Confirmar Pasar Turno Y/N{reset} ")
                        pasar = siono(pasar)
                                
                    elif opc == 6: # FALTA IMPLEMENTAR ##############################################################################
                        jugador.perder
                        PasarTurno = False

    elif opc == 3:
        salir = True
        print(f"{exito}HASTA LA PROXIMA{reset}")