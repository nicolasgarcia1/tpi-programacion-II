from unidadGuerra import UnidadGuerra
from unidadRecoleccion import UnidadRecoleccion
from item import Item

memory_card = {
    'ashenvale': {
        'recursos': {
            'cantidadMadera': 2000,
            'cantidadOro': 2000,
        },
        'jugadores': [
            {
                'nombreJugador': 'Macho',
                'color': 'rojo',
                'raza': 'humano',
                'oro': 200,
                'madera': 200,
            },
            {
                'nombreJugador': 'Ramon',
                'color': 'azul',
                'raza': 'orco',
                'oro': 200,
                'madera': 200,
            },
        ],
        'edificios': {
            'precioCompraMadera': 50,
            'vida': 3000,
            'poblacion': 2,
        },
    },
    'stranglethorn vale': {
        'recursos': {
            'cantidadMadera': 1500,
            'cantidadOro': 1500,
        },
        'jugadores': [
            {
                'nombreJugador': 'EL MAS CAPO',
                'color': 'rojo',
                'raza': 'humano',
                'oro': 200,
                'madera': 200,
            },
            {
                'nombreJugador': 'Pedro',
                'color': 'azul',
                'raza': 'orco',
                'oro': 200,
                'madera': 200,
            },
            {
                'nombreJugador': 'EL PRO',
                'color': 'verde',
                'raza': 'elfo',
                'oro': 200,
                'madera': 200,
            },
        ],
        'edificios': {
            'precioCompraMadera': 75,
            'vida': 3000,
            'poblacion': 2,
        },
    },
    'lordaeron': {
        'recursos': {
            'cantidadMadera': 5000,
            'cantidadOro': 5000,
        },
        'jugadores': [
            {
                'nombreJugador': 'yo',
                'color': 'rojo',
                'raza': 'humano',
                'oro': 500,
                'madera': 500,
            },
            {
                'nombreJugador': 'Paul',
                'color': 'azul',
                'raza': 'orco',
                'oro': 500,
                'madera': 500,
            },
            {
                'nombreJugador': 'god',
                'color': 'verde',
                'raza': 'elfo',
                'oro': 500,
                'madera': 500,
            },
        ],
        'edificios': {
            'precioCompraMadera': 50,
            'vida': 2000,
            'poblacion': 1,
        },
    },
}

Unidades = [UnidadGuerra(tipoUnidad="Soldado Ligero", tipoDaño="Normal", tipoDefensa="Sin Armadura"),
            UnidadGuerra(tipoUnidad="Caballero de Plata", tipoDaño="Normal", tipoDefensa="Armadura Ligera"),
            UnidadGuerra(tipoUnidad="Vanguardia de Hierro", tipoDaño="Normal", tipoDefensa="Armadura Media"),
            UnidadGuerra(tipoUnidad="Coloso de Acero", tipoDaño="Normal", tipoDefensa="Armadura Pesada"),
            UnidadGuerra(tipoUnidad="Asesino Furtivo", tipoDaño="Perforante", tipoDefensa="Sin Armadura"),
            UnidadGuerra(tipoUnidad="Lancero Veloz", tipoDaño="Perforante", tipoDefensa="Armadura Ligera"),
            UnidadGuerra(tipoUnidad="Táctico Blindado", tipoDaño="Perforante", tipoDefensa="Armadura Media"),
            UnidadGuerra(tipoUnidad="Demoledor Implacable", tipoDaño="Perforante", tipoDefensa="Armadura Pesada"),
            UnidadGuerra(tipoUnidad="Bombardero Escarlata", tipoDaño="Asedio", tipoDefensa="Sin Armadura"),
            UnidadGuerra(tipoUnidad="Catapulta de Bronce", tipoDaño="Asedio", tipoDefensa="Armadura Ligera"),
            UnidadGuerra(tipoUnidad="Balista de Plomo", tipoDaño="Asedio", tipoDefensa="Armadura Media"),
            UnidadGuerra(tipoUnidad="Mortero de Ébano", tipoDaño="Asedio", tipoDefensa="Armadura Pesada"),
            UnidadGuerra(tipoUnidad="Hechicero Arcano", tipoDaño="Magico", tipoDefensa="Sin Armadura"),
            UnidadGuerra(tipoUnidad="Encantador Élfico", tipoDaño="Magico", tipoDefensa="Armadura Ligera"),
            UnidadGuerra(tipoUnidad="Invocador Celestial", tipoDaño="Magico", tipoDefensa="Armadura Media"),
            UnidadGuerra(tipoUnidad="Archimago Dorado", tipoDaño="Magico", tipoDefensa="Armadura Pesada"),
            UnidadRecoleccion(tipoUnidad="Recolector")]

Items = [Item(nombre="Armadura del Guerrero", vida=20, daño=20, defensa=20),
         Item(nombre="Coraza del Campeón", vida=20, daño=20, defensa=20),
         Item(nombre="Túnica del Gladiador", vida=20, daño=20, defensa=20),
         Item(nombre="Espada del Berserker", vida=30, daño=30),
         Item(nombre="Lanza del Asesino", vida=30, daño=30),
         Item(nombre="Maza del Destructor", vida=30, daño=30),
         Item(nombre="Escudo del Guardián", vida=30, defensa=30),
         Item(nombre="Muro del Protector", vida=30, defensa=30),
         Item(nombre="Barrera del Defensor", vida=30, defensa=30),
         Item(nombre="Hacha del Conquistador", daño=30, defensa=30),
         Item(nombre="Martillo del Titán", daño=30, defensa=30),
         Item(nombre="Espadón del Dominador", daño=30, defensa=30)]