import Piloto

__author__ = 'polmdor'

class Escuderia():
    def __init__(self, nombre, sede = None, chasis = None, motor = None, neumaticos = None, primeratemp = None, fechacrea = None):
        self.nombre = nombre
        self.sede = sede
        self.chasis = chasis
        self.motor = motor
        self.neumaticos = neumaticos
        self.primeraTemp = primeratemp
        self.fechaCrea = fechacrea
        self.pilotos = []
        self.pilotosActivos = []
        self.p = None

    def agregarPiloto(self, piloto):
        if (isinstance(piloto, Piloto)):
            self.pilotos.append(piloto)
        else:
            print "Error al agregar piloto a la escuderia " + self.nombre + "."

    def eliminarPiloto(self, piloto):
        if (isinstance(piloto, Piloto) and (piloto in self.pilotos)):
            self.pilotos.remove(piloto)
        else:
            print "Error al eliminar piloto de la escuderia " + self.nombre + "."

    def definirPilotosActivos(self, piloto1, piloto2):
        if (isinstance(piloto1, Piloto) and isinstance(piloto2, Piloto)):
            self.pilotosActivos.append(piloto1)
            self.pilotosActivos.append(piloto2)
        else:
            print "Error al definir pilotos activos de la escuderia " + self.nombre + "."