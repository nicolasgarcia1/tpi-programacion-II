from partida import Partida
from unidadGuerra import UnidadGuerra
from unidadRecoleccion import UnidadRecoleccion
from item import Item

partidas = [
    Partida("Deadwind Pass",      1000,  1000),
    Partida("Ashen Vale",         2000,  2000),
    Partida("Stranglethorn Vale", 3000,  3000),
    Partida("Lordearon",          4000,  4000),
    Partida("Durotar",            5000,  5000),
    Partida("Tirisfal Glades",    6000,  6000),
    Partida("Duskwood",           7000,  7000),
    Partida("Elwynn Forest",      8000,  8000),
    Partida("Westfall",           9000,  9000),
    Partida("Redridge Mountains", 10000, 10000),
]

unidades = [
    UnidadGuerra("Soldado Ligero",       "Normal",     100, "Sin Armadura",    100, 200),
    UnidadGuerra("Caballero de Plata",   "Normal",     100, "Armadura Ligera", 125, 225),
    UnidadGuerra("Vanguardia de Hierro", "Normal",     100, "Armadura Media",  150, 250),
    UnidadGuerra("Coloso de Acero",      "Normal",     100, "Armadura Pesada", 175, 275),
    UnidadGuerra("Asesino Furtivo",      "Perforante", 125, "Sin Armadura",    100, 225),
    UnidadGuerra("Lancero Veloz",        "Perforante", 125, "Armadura Ligera", 125, 250),
    UnidadGuerra("Táctico Blindado",     "Perforante", 125, "Armadura Media",  150, 275),
    UnidadGuerra("Demoledor Implacable", "Perforante", 125, "Armadura Pesada", 175, 300),
    UnidadGuerra("Bombardero Escarlata", "Asedio",     150, "Sin Armadura",    100, 250),
    UnidadGuerra("Catapulta de Bronce",  "Asedio",     150, "Armadura Ligera", 125, 275),
    UnidadGuerra("Balista de Plomo",     "Asedio",     150, "Armadura Media",  150, 300),
    UnidadGuerra("Mortero de Ébano",     "Asedio",     150, "Armadura Pesada", 175, 325),
    UnidadGuerra("Hechicero Arcano",     "Magico",     175, "Sin Armadura",    100, 275),
    UnidadGuerra("Encantador Élfico",    "Magico",     175, "Armadura Ligera", 125, 300),
    UnidadGuerra("Invocador Celestial",  "Magico",     175, "Armadura Media",  150, 325),
    UnidadGuerra("Archimago Dorado",     "Magico",     175, "Armadura Pesada", 175, 350),
    UnidadRecoleccion()
]

items = [
    Item("Armadura del Guerrero",  350, 20, 20, 20),
    Item("Coraza del Campeón",     350, 20, 20, 20),
    Item("Túnica del Gladiador",   350, 20, 20, 20),
    Item("Espada del Berserker",   350, 30, 30, 0),
    Item("Lanza del Asesino",      350, 30, 30, 0),
    Item("Maza del Destructor",    350, 30, 30, 0),
    Item("Escudo del Guardián",    350, 30, 0,  30),
    Item("Muro del Protector",     350, 30, 0,  30),
    Item("Barrera del Defensor",   350, 30, 0,  30),
    Item("Hacha del Conquistador", 350, 0,  30, 30),
    Item("Martillo del Titán",     350, 0,  30, 30),
    Item("Espadón del Dominador",  350, 0,  30, 30)
]

colores = ["Gris","Marron","Rojo","Naranja","Amarillo","Verde","Lima","Azul","Celeste","Violeta","Magenta","Rosa"]

razas = ["Humanos","Orcos","Muertos Vivientes","Elfos Oscuros"]