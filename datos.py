from partida import Partida
from unidadGuerra import UnidadGuerra
from unidadRecoleccion import UnidadRecoleccion
from item import Item

partidas = [
    Partida("Deadwind Pass",      10000,  10000),
    Partida("Ashen Vale",         20000,  20000),
    Partida("Stranglethorn Vale", 30000,  30000),
    Partida("Lordearon",          40000,  40000),
    Partida("Durotar",            50000,  50000),
    Partida("Tirisfal Glades",    60000,  60000),
    Partida("Duskwood",           70000,  70000),
    Partida("Elwynn Forest",      80000,  80000),
    Partida("Westfall",           90000,  90000),
    Partida("Redridge Mountains", 100000, 100000),
]

unidades = [
    UnidadGuerra("Soldado Ligero",       "Normal",     100, "Sin Armadura",    0, 200),
    UnidadGuerra("Caballero de Plata",   "Normal",     100, "Armadura Ligera", 25, 225),
    UnidadGuerra("Vanguardia de Hierro", "Normal",     100, "Armadura Media",  50, 250),
    UnidadGuerra("Coloso de Acero",      "Normal",     100, "Armadura Pesada", 75, 275),
    UnidadGuerra("Asesino Furtivo",      "Perforante", 125, "Sin Armadura",    0, 225),
    UnidadGuerra("Lancero Veloz",        "Perforante", 125, "Armadura Ligera", 25, 250),
    UnidadGuerra("Táctico Blindado",     "Perforante", 125, "Armadura Media",  50, 275),
    UnidadGuerra("Demoledor Implacable", "Perforante", 125, "Armadura Pesada", 75, 300),
    UnidadGuerra("Bombardero Escarlata", "Asedio",     150, "Sin Armadura",    0, 250),
    UnidadGuerra("Catapulta de Bronce",  "Asedio",     150, "Armadura Ligera", 25, 275),
    UnidadGuerra("Balista de Plomo",     "Asedio",     150, "Armadura Media",  50, 300),
    UnidadGuerra("Mortero de Ébano",     "Asedio",     150, "Armadura Pesada", 75, 325),
    UnidadGuerra("Hechicero Arcano",     "Magico",     175, "Sin Armadura",    0, 275),
    UnidadGuerra("Encantador Élfico",    "Magico",     175, "Armadura Ligera", 25, 300),
    UnidadGuerra("Invocador Celestial",  "Magico",     175, "Armadura Media",  50, 325),
    UnidadGuerra("Archimago Dorado",     "Magico",     175, "Armadura Pesada", 75, 350),
    UnidadRecoleccion()
]

items = [
    Item("Armadura del Guerrero",  350, 30, 30, 20),
    Item("Coraza del Campeón",     350, 30, 30, 20),
    Item("Túnica del Gladiador",   350, 30, 30, 20),
    Item("Espada del Berserker",   350, 40, 40, 0),
    Item("Lanza del Asesino",      350, 40, 40, 0),
    Item("Maza del Destructor",    350, 40, 40, 0),
    Item("Escudo del Guardián",    350, 50, 0,  30),
    Item("Muro del Protector",     350, 50, 0,  30),
    Item("Barrera del Defensor",   350, 50, 0,  30),
    Item("Hacha del Conquistador", 350, 0,  50, 30),
    Item("Martillo del Titán",     350, 0,  50, 30),
    Item("Espadón del Dominador",  350, 0,  50, 30)
]

colores = ["Gris","Marron","Rojo","Naranja","Amarillo","Verde","Lima","Azul","Celeste","Violeta","Magenta","Rosa"]

razas = ["Humanos","Orcos","Muertos Vivientes","Elfos Oscuros"]