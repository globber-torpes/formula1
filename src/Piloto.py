import re
import Error

class Piloto():
    def __init__(self, idpiloto, nombre = None, apellidos = None, equipo = None, equipoAnterior = None, nacionalidad = None, fechanac = None):
        """
        Contructor de pilotos

        """
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
        """
        Metodo ToString
        Devuelve todos los datos del piloto, identificador, nombre, apellidos, equipo,equipo anterior,
        nacionalidad, fecha de nacimiento.

        :return: cadena con la informacion de un piloto
        :rtype: string
        """
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
