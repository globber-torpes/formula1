class Circuito():
    def __init__(self, nombre, ubicacion = None, longitud = None, numVueltas = None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.longitud = longitud
        self.numVueltas = numVueltas

    def __str__(self):
        tostring = "Datos del circuito: \nNombre del circuito: " + self.nombre
        if(self.ubicacion != None):
            tostring += "\nUbicacion: " + self.ubicacion
        if(self.longitud != None):
            tostring += "\nLongitud: " + str(self.longitud) + "km"
        if(self.numVueltas != None):
            tostring += "\nNumero de Vueltas: " + str(self.numVueltas)
        return tostring + "\n"