__author__ = 'polmdor'

class Piloto():
    def __init__(self, idpiloto, nombre = None, apellidos = None, equipo = None, equipoAnterior = None, nacionalidad = None, fechanac = None):
        self.idPiloto = idpiloto
        self.nombre = nombre
        self.apellidos = apellidos
        self.equipo = equipo
        self.equipoAnterior = equipoAnterior
        self.nacionalidad = nacionalidad
        self.fechanac = fechanac
        self.p = None

    def __str__(self):
        tostring = "Datos del piloto: \n\tIdentificador del piloto: " + str(self.idPiloto) + "\n"

        if(self.nombre != None):
            tostring += "\tNombre completo: " + self.nombre
        if(self.apellidos != None):
            tostring += " " + self.apellidos
        if(self.equipo != None):
            tostring += "\n\tEquipo: " + self.equipo
        if(self.equipoAnterior != None):
            tostring += "\n\tEquipo Anterior: " + self.equipoAnterior
        if(self.nacionalidad != None):
            tostring += "\n\tNacionalidad: " + self.nacionalidad
        if(self.fechanac != None):
            tostring += "\n\tFecha de Nacimiento: " + self.fechanac

        return tostring
