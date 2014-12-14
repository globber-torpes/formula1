from Piloto import Piloto
from Escuderia import Escuderia
from Circuito import Circuito
from CampeonatoMundial import CampeonatoMundial
from datetime import date


class Formula1():
    """
    Modela una liga de formula 1

    :author: Francisco Lopez Baena
    :version: 1
    """
    campeonatos_mundiales = {}
    circuitos = {}
    escuderias = {}
    pilotos = {}

    def __init__(self):
        """
        descripcion breve: constructor

        descripcion detallada: inicializador de la clase formula1

        :return: no devuelve nada
        """
        self.campeonatos_mundiales = {}
        self.circuitos = {}
        self.escuderias = {}
        self.pilotos = {}

    def crear_campeonato_mundial(self, edicion, escuderias=None):
        """
        descripcion breve: crear campeonato

        descripcion detallada: metodo para crear un campeonato mundial

        :param edicion: anno del mundial
        :param escuderias: escuderias que participan en el mundial
        :return: campeonato_mundial
        """
        if escuderias is None:
            escuderias = self.escuderias
        campeonato_mundial = CampeonatoMundial(edicion, escuderias)
        self.agregar_campeonato_mundial(campeonato_mundial)
        return campeonato_mundial

    def agregar_campeonato_mundial(self, campeonato_mundial):
        """
        descripcion breve: agregar campeonato

        descripcion detallada: metodo para agregar un campeonato mundial

        :param campeonato_mundial: lista de campeonatos en un mundial
        :return: no devuelve nada
        """
        if isinstance(campeonato_mundial, CampeonatoMundial) and \
                (campeonato_mundial.edicion not in self.campeonatos_mundiales):
            self.campeonatos_mundiales[campeonato_mundial.edicion] = campeonato_mundial
            return True
        else:
            print ("Error al agregar el Campeonato Mundial edicion " + str(campeonato_mundial.edicion) + ".")
            return False

    def eliminar_campeonato_mundial(self, campeonato_mundial):
        """
        descripcion breve: eliminar campeonato

        descripcion detallada: metodo para eliminar un campeonato mundial

        :param campeonato_mundial: lista de campeonatos en un mundial
        :return: no devuelva nada
        """
        if isinstance(campeonato_mundial, CampeonatoMundial) and \
                (campeonato_mundial.edicion in self.campeonatos_mundiales):
            del self.campeonatos_mundiales[campeonato_mundial.edicion]
            return True
        else:
            print ("Error al eliminar el Campeonato Mundial edicion " + str(campeonato_mundial.edicion) + ".")
            return False

    def crear_escuderia(self, nombre, sede=None, chasis=None, motor=None, neumaticos=None,
                        primera_temp=True, fecha_crea=date.today()):
        """
        descripcion breve: crear escuderia

        descripcion detallada: metodo para crear una escuderia

        :param nombre: nombre escuderia
        :param sede: sede de la escuderia
        :param chasis: chasis de la escuderia
        :param motor: motor de la escuderia
        :param neumaticos: neumaticos de la escuderia
        :param primera_temp: primera temporada de la escuderia
        :param fecha_crea: fecha de creacion de la escuderia
        :return: escuderia
        """
        escuderia = Escuderia(nombre, sede, chasis, motor, neumaticos, primera_temp, fecha_crea)
        self.agregar_escuderia(escuderia)
        return escuderia

    def agregar_escuderia(self, escuderia):
        """
        descripcion breve: agregar escuderia

        descripcion detallada: metodo para agregar escuderias

        :param escuderia: escuderia
        :return: no devuelve nada
        """
        if isinstance(escuderia, Escuderia) and (escuderia.nombre not in self.escuderias):
            self.escuderias[escuderia.nombre] = escuderia
        else:
            print ("Error al agregar la escuderia " + escuderia.nombre + ".")

    def eliminar_escuderia(self, escuderia):
        """
        descripcion breve: eliminar escuderia

        descripcion detallada: metodo para eliminar escuderias

        :param escuderia: escuderia
        :return: no devuelve nada
        """
        if isinstance(escuderia, Escuderia) and (escuderia.edicion in self.escuderias):
            del self.escuderias[escuderia.nombre]
        else:
            print ("Error al eliminar la escuderia " + escuderia.nombre + ".")

    def crear_piloto(self, id_pil, nombre=None, apellidos=None, equipo=None,
                     equipo_anterior=None, nacionalidad=None, fecha_nac=None):
        """
        descripcion breve: crear piloto

        descripcion detallada: metodo para crear pilotos

        :param id_pil: identificacion del piloto
        :param nombre: nombre del piloto
        :param apellidos: apellidos del piloto
        :param equipo: equipo al que pertenece el piloto
        :param equipo_anterior: equipo al que pertenecio el piloto anteriormente
        :param nacionalidad: nacionalidad del piloto
        :param fecha_nac: fecha de nacimiento del  piloto
        :return: piloto
        """
        piloto = Piloto(id_pil, nombre, apellidos, equipo, equipo_anterior, nacionalidad, fecha_nac)
        self.agregar_piloto(piloto)
        if equipo and self.escuderias[equipo]:
            self.escuderias[equipo].agregar_piloto(piloto)
        return piloto

    def agregar_piloto(self, piloto):
        """
        descripcion breve: agregar piloto

        descripcion detallada: metodo para agregar pilotos

        :param piloto: piloto
        :return: no devuelve nada
        """
        if isinstance(piloto, Piloto) and (piloto.idPiloto not in self.pilotos):
            self.pilotos[piloto.idPiloto] = piloto
        else:
            print ("Error al agregar al piloto " + piloto.nombre + " " + piloto.apellidos + ".")

    def eliminar_piloto(self, piloto):
        """
        descripcion breve: eliminar piloto

        descripcion detallada: metodo para eliminar piloto

        :param piloto: piloto
        :return: no devuelve nada
        """
        if isinstance(piloto, Piloto) and (piloto.idPiloto in self.pilotos):
            del self.pilotos[piloto.idPiloto]
        else:
            print ("Error al eliminar al piloto " + piloto.nombre + " " + piloto.apellidos + ".")

    def crear_circuito(self, nombre, ubicacion=None, longitud=None, num_vueltas=None):
        """
        descripcion breve: crear circuito

        descripcion detallada: metodo para crear circuito

        :param nombre: nombre del circuito
        :param ubicacion: pais donde se ubica el circuito
        :param longitud: longitud del circuito
        :param num_vueltas: numeros de vueltas que se dan al circuito
        :return:
        """
        circuito = Circuito(nombre, ubicacion, longitud, num_vueltas)
        self.agregar_circuito(circuito)
        return circuito

    def agregar_circuito(self, circuito):
        """
        descripcion breve: agregar circuito

        descripcion detallada: metodo para agregar circuitos

        :param circuito: circuito
        :return: no devuelve nada
        """
        if isinstance(circuito, Circuito) and (circuito.nombre not in self.circuitos):
            self.circuitos[circuito.nombre] = circuito
        else:
            print ("Error al agregar el circuito " + circuito.nombre + ".")

    def eliminar_circuito(self, circuito):
        """
        descripcion breve: eliminar circuito

        descripcion detallada: metodo para eliminar circuitos

        :param circuito: circuito
        :return: no devuelve nada
        """
        if isinstance(circuito, Circuito) and (circuito.nombre in self.circuitos):
            del self.circuitos[circuito.nombre]
        else:
            print ("Error al eliminar el circuito " + circuito.nombre + ".")

    def print_pilotos(self):
        """
        descripcion breve: imprimir pilotos

        descripcion detallada: metodo para imprimir los pilotos

        :return: no devuelve nada
        """
        for piloto in self.pilotos.values():
            print piloto

    def print_escuderias(self):
        """
        descripcion breve: imprimir escuderia

        descripcion detallada: metodo para imprimir escuderias

        :return: no devuelve nada
        """
        for escuderia in self.escuderias.values():
            print escuderia

    def print_circuitos(self):
        """
        descripcion breve: imprimir circuitos

        descripcion detallada: metodo para imprimir circuitos

        :return: no devuelve nada
        """
        for circuito in self.circuitos.values():
            print circuito

    def print_campeonatos_mundiales(self):
        """
        descripcion breve: imprimir campeonatos

        descripcion detallada: metodo para imprimir campeonatos mundiales

        :return: no devuelve nada
        """
        for gp in self.campeonatos_mundiales.values():
            print gp

    def demo(self):
        """
        descripcion breve: probar

        descripcion detallada: metodo para probar los metodos anteriores

        :return: no devuelve nada
        """

        #Creacion de escuderias
        e1 = self.crear_escuderia("Ferrari", "Maranello")
        e2 = self.crear_escuderia("Red Bull")
        e3 = self.crear_escuderia("Mercedes",chasis="Mercedes F1 W05", motor="Mercedes PU106A Hybrid V6", neumaticos="Pirelli")

        #Creacion de pilotos
        p1 = self.crear_piloto("ALO", "Fernando", "Alonso", "Ferrari", "Mercedes", "Espaniola", "29/7/81")
        p2 = self.crear_piloto("RAI", "Kimi", "Raikkonen", "Ferrari")
        p3 = self.crear_piloto("RIC", "Daniel", "Ricciardo", "Red Bull")
        p4 = self.crear_piloto("VET", "Sebastian", "Vettel", "Red Bull")
        p5 = self.crear_piloto("SCH", "Michael", "Schumacher", "Ferrari")
        p7 = self.crear_piloto("HAM", "Lewis", "Hamilton", "Mercedes")
        p8 = self.crear_piloto("ROS", "Nico", "Rosberg", "Mercedes")

        #imprimiendo pilotos y escuderias
        self.print_pilotos()
        self.print_escuderias()

        #Creando circuitos
        c1 = self.crear_circuito("Red Bull Ring", "Spielberg", 4326)
        c2 = self.crear_circuito("Circuito de Sochi", "Sochi")
        c3 = self.crear_circuito("Internacional de Corea", "Yeongam")

        #imprimiendo circuitos
        self.print_circuitos()

        #creando campeonato mundial
        cm1 = self.crear_campeonato_mundial(2014)

        #imprimiendo campeonato mundial
        self.print_campeonatos_mundiales()

        #creando grandes premios del campeonato mundial
        gp1 = cm1.crear_gran_premio("Gran Premio de Austria", c1)
        gp2 = cm1.crear_gran_premio("Gran Premio de Rusia", c2)
        gp3 = cm1.crear_gran_premio("Gran Premio de Corea del Sur", c3)

        self.print_campeonatos_mundiales()

        #Simulando grandes premios
        cm1.simular_gran_premio(gp1)
        cm1.simular_gran_premio(gp2)

        #Simulando accidente y cambio de piloto
        p6 = self.crear_piloto("AUX", "Piloto", "Auxiliar de Prueba")
        print ("El piloto " + p2.nombre + " " + p2.apellidos +
               " ha sufrido un accidente. Se sustituira por el piloto " + p6.nombre + " " + p6.apellidos + "\n")
        e1.sustituir_piloto(p2, p6)

        cm1.simular_gran_premio(gp3)

        cm1.print_grandes_premios()
        self.print_campeonatos_mundiales()

