from Piloto import Piloto

class Escuderia():
    def __init__(self, nombre, sede = None, chasis = None, motor = None, neumaticos = None, primeratemp = None, fechacrea = None):
        self.nombre = nombre
        self.sede = sede
        self.chasis = chasis
        self.motor = motor
        self.neumaticos = neumaticos
        self.primeraTemp = primeratemp
        self.fechaCrea = fechacrea
        self.pilotos = {}
        self.pilotosActivos = {}

    def agregarPiloto(self, piloto):
        if (isinstance(piloto, Piloto) and (piloto.idPiloto not in self.pilotos)):
            piloto.equipo = self.nombre
            self.pilotos[piloto.idPiloto] = piloto
            if len(self.pilotosActivos)<2 and piloto.idPiloto not in self.pilotosActivos:
                self.pilotosActivos[piloto.idPiloto] = piloto
        else:
            print "Error al agregar piloto a la escuderia " + self.nombre + "."

    def eliminarPiloto(self, piloto):
        if (isinstance(piloto, Piloto) and (piloto.idPiloto in self.pilotos)):
            piloto.equipo = None
            piloto.equipoAnterior = self.nombre
            del self.pilotos[piloto.idPiloto]
            if piloto.idPiloto in self.pilotosActivos:
                del self.pilotosActivos[piloto.idPiloto]
                if len(self.pilotosActivos)<2:
                    print "Atencion, el piloto eliminado estaba marcado como activo. Redefina los pilotos activos."
        else:
            print "Error al eliminar piloto de la escuderia " + self.nombre + "."

    def definirPilotosActivos(self, piloto1, piloto2):
        if (isinstance(piloto1, Piloto) and isinstance(piloto2, Piloto)):
            self.pilotosActivos.clear()
            self.pilotosActivos[piloto1.idPiloto] = piloto1
            self.pilotosActivos[piloto2.idPiloto] = piloto2
        else:
            print "Error al definir pilotos activos de la escuderia " + self.nombre + "."

    def sustituirPiloto(self, piloto1, piloto2):
        if (isinstance(piloto1, Piloto) and isinstance(piloto2, Piloto)):
            if(piloto1.idPiloto in self.pilotosActivos.keys()):
                del self.pilotosActivos[piloto1.idPiloto]
                self.pilotosActivos[piloto2.idPiloto] = piloto2
            self.eliminarPiloto(piloto1)
            self.agregarPiloto(piloto2)
        else:
            print "Error al sustituir pilotos en la escuderia " + self.nombre + "."

    def __str__(self):
        tostring = "Datos de la Escuderia: \nNombre de la escuderia: " + str(self.nombre)
        if(self.sede != None):
            tostring += "\nUbicacion de la sede: " + self.sede
        if(self.chasis != None):
            tostring += "\nChasis utilizado: " + self.chasis
        if(self.motor != None):
            tostring += "\nMotor montado: " + self.motor
        if(self.neumaticos != None):
            tostring += "\nMarca de neumaticos: " + self.neumaticos
        if(self.primeraTemp != None):
            tostring += "\nPrimera temporada?: " + str(self.primeraTemp)
        if(self.fechaCrea != None):
            tostring += "\nFecha de creacion de la Escuderia: " + str(self.fechaCrea)
        if(self.pilotos):
            tostring += "\nPilotos en plantilla: \n\t" + str(self.pilotos.keys())
        if(self.pilotosActivos):
            tostring += "\nPilotos activos: \n\t" + str(self.pilotosActivos.keys())
        return tostring + "\n"