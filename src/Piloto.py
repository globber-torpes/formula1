import re
import Error

class Piloto():

    def __init__(self, idpiloto, nombre = None, apellidos = None, equipo = None, equipoAnterior = None, nacionalidad = None, fechanac = None):
        regex = re.compile("([A-Z][A-Z][A-Z])")
        r = regex.search(idpiloto)
        if r is not None:
            self.idPiloto = idpiloto
            self.nombre = nombre
            self.apellidos = apellidos
            self.equipo = equipo
            self.equipoAnterior = equipoAnterior
            self.nacionalidad = nacionalidad
            self.fechanac = fechanac
        else:
            raise Error.FormatoException("idpiloto")

    def __str__(self):
        tostring = "Datos del piloto: \nIdentificador del piloto: " + str(self.idPiloto)

        if(self.nombre != None):
            tostring += "\nNombre completo: " + self.nombre
        if(self.apellidos != None):
            tostring += " " + self.apellidos
        if(self.equipo != None):
            tostring += "\nEquipo: " + self.equipo
        if(self.equipoAnterior != None):
            tostring += "\nEquipo Anterior: " + self.equipoAnterior
        if(self.nacionalidad != None):
            tostring += "\nNacionalidad: " + self.nacionalidad
        if(self.fechanac != None):
            tostring += "\nFecha de Nacimiento: " + self.fechanac

        return tostring + "\n"
        
    def get_id_piloto(self):
        return str(self.idPiloto)