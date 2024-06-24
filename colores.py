gris = "\x1B[38;2;128;128;128m"
marron = "\x1B[38;2;128;64;0m"
rojo = "\x1B[38;2;255;128;128m"
naranja = "\x1B[38;2;255;192;64m"
amarillo = "\x1B[38;2;255;255;128m"
verde = "\x1B[38;2;0;128;0m"
lima = "\x1B[38;2;128;192;0m"
azul = "\x1B[38;2;0;128;255m"
celeste = "\x1B[38;2;0;192;192m"
violeta = "\x1B[38;2;128;0;255m"
magenta = "\x1B[38;2;192;0;128m"
rosa = "\x1B[38;2;255;192;255m"
exito = "\x1B[38;2;128;255;128m"
neutro = "\x1B[38;2;255;255;0m"
error = "\x1B[38;2;255;0;0m"  
reset = "\x1B[0m"

def cambiarColor(color):
    if color == "Gris":
        return gris
    elif color == "Marron":
        return marron
    elif color == "Rojo":
        return rojo
    elif color == "Naranja":
        return naranja
    elif color == "Amarillo":
        return amarillo
    elif color == "Verde":
        return verde
    elif color == "Lima":
        return lima
    elif color == "Azul":
        return azul
    elif color == "Celeste":
        return celeste
    elif color == "Violeta":
        return violeta
    elif color == "Magenta":
        return magenta
    elif color == "Rosa":
        return rosa