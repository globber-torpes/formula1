from Piloto import Piloto
from Escuderia import Escuderia
from Circuito import Circuito
from CampeonatoMundial import CampeonatoMundial
from datetime import date

class Formula1():
    campeonatosMundiales = {}
    circuitos = {}
    escuderias = {}
    pilotos = {}

    def __init__(self):
        self.campeonatosMundiales = {}
        self.circuitos = {}
        self.escuderias = {}
        self.pilotos = {}

    def crearCampeonatoMundial(self, edicion, escuderias = None):
        if escuderias is None:
            escuderias = self.escuderias
        campeonatoMundial = CampeonatoMundial(edicion, escuderias)
        self.agregarCampeonatoMundial(campeonatoMundial)
        return campeonatoMundial

    def agregarCampeonatoMundial(self, campeonatoMundial):
        if (isinstance(campeonatoMundial, CampeonatoMundial) and (campeonatoMundial.edicion not in self.campeonatosMundiales)):
            self.campeonatosMundiales[campeonatoMundial.edicion] = campeonatoMundial
        else:
            print "Error al agregar el Campeonato Mundial edicion " + str(campeonatoMundial.edicion) + "."

    def eliminarCampeonatoMundial(self, campeonatoMundial):
        if (isinstance(campeonatoMundial, CampeonatoMundial) and (campeonatoMundial.edicion in self.campeonatosMundiales)):
            del self.campeonatosMundiales[campeonatoMundial.edicion]
        else:
            print "Error al eliminar el Campeonato Mundial edicion " + str(campeonatoMundial.edicion) + "."

    def crearEscuderia(self, nombre, sede = None, chasis = None, motor = None, neumaticos = None, primeratemp = True, fechacrea = date.today()):
        escuderia = Escuderia(nombre, sede, chasis, motor, neumaticos, primeratemp, fechacrea)
        self.agregarEscuderia(escuderia)
        return escuderia

    def agregarEscuderia(self, escuderia):
        if (isinstance(escuderia, Escuderia) and (escuderia.nombre not in self.escuderias)):
            self.escuderias[escuderia.nombre] = escuderia
        else:
            print "Error al agregar la escuderia " + escuderia.nombre + "."

    def eliminarEscuderia(self, escuderia):
        if (isinstance(escuderia, Escuderia) and (escuderia.edicion in self.escuderias)):
            del self.escuderias[escuderia.nombre]
        else:
            print "Error al eliminar la escuderia " + escuderia.nombre + "."

    def crearPiloto(self, idpiloto, nombre = None, apellidos = None, equipo = None, equipoAnterior = None, nacionalidad = None, fechanac = None):
        piloto = Piloto(idpiloto,nombre,apellidos,equipo,equipoAnterior,nacionalidad,fechanac)
        self.agregarPiloto(piloto)
        if equipo and self.escuderias[equipo]:
            self.escuderias[equipo].agregarPiloto(piloto)
        return piloto

    def agregarPiloto(self, piloto):
        if (isinstance(piloto, Piloto) and (piloto.idPiloto not in self.pilotos)):
            self.pilotos[piloto.idPiloto] = piloto
        else:
            print "Error al agregar al piloto " + piloto.nombre + " " + piloto.apellidos +"."

    def eliminarPiloto(self, piloto):
        if (isinstance(piloto, Piloto) and (piloto.idPiloto in self.pilotos)):
            del self.pilotos[piloto.idPiloto]
        else:
            print "Error al eliminar al piloto " + piloto.nombre + " " + piloto.apellidos +"."

    def crearCircuito(self, nombre, ubicacion = None, longitud = None, numVueltas = None):
        circuito = Circuito(nombre,ubicacion,longitud,numVueltas)
        self.agregarCircuito(circuito)
        return circuito

    def agregarCircuito(self, circuito):
        if (isinstance(circuito, Circuito) and (circuito.nombre not in self.circuitos)):
            self.circuitos[circuito.nombre] = circuito
        else:
            print "Error al agregar el circuito " + circuito.nombre + "."

    def eliminarCircuito(self, circuito):
        if (isinstance(circuito, Circuito) and (circuito.nombre in self.circuitos)):
            del self.circuitos[circuito.nombre]
        else:
            print "Error al eliminar el circuito " + circuito.nombre + "."

    def printPilotos(self):
        for piloto in self.pilotos.values():
            print piloto

    def printEscuderias(self):
        for escuderia in self.escuderias.values():
            print escuderia

    def printCircuitos(self):
        for circuito in self.circuitos.values():
            print circuito

    def printCampeonatosMundiales(self):
        for gp in self.campeonatosMundiales.values():
            print gp

    def demo(self):

        e1 = self.crearEscuderia("Ferrari","Maranello")
        e2 = self.crearEscuderia("Red Bull")

        p1 = self.crearPiloto("ALO","Fernando","Alonso","Ferrari")
        p2 = self.crearPiloto("MAS","Felipe","Massa","Ferrari")
        p3 = self.crearPiloto("WEB","Mark", "Webber", "Red Bull")
        p4 = self.crearPiloto("VET","Sebastien", "Vettel", "Red Bull")
        p5 = self.crearPiloto("SCH","Michael", "Schumacher", "Ferrari")

        self.printPilotos()

        self.printEscuderias()

        c1 = self.crearCircuito("Red Bull Ring","Spielberg",4326)
        c2 = self.crearCircuito("Circuito de Sochi", "Sochi")
        c3 = self.crearCircuito("Internacional de Corea", "Yeongam")

        self.printCircuitos()

        cm1 = self.crearCampeonatoMundial(2014)

        self.printCampeonatosMundiales()

        gp1 = cm1.crearGranPremio("Gran Premio de Austria",c1)
        gp2 = cm1.crearGranPremio("Gran Premio de Rusia", c2)

        cm1.simularGranPremio(gp1)
        cm1.simularGranPremio(gp2)

        p6 = self.crearPiloto("AUX", "Piloto", "Auxiliar de Prueba")
        print "El piloto " + p2.nombre + " " + p2.apellidos + " ha sufrido un accidente. Se sustituira por el piloto " + p6.nombre + " " + p6.apellidos + "\n"
        e1.sustituirPiloto(p2, p6)

        gp3 = cm1.crearGranPremio("Gran Premio de Corea del Sur", c3)
        cm1.simularGranPremio(gp3)

        cm1.printGrandesPremios()
        self.printCampeonatosMundiales()

