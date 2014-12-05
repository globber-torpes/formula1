class Circuito():
    def __init__(self, nombre, ubicacion=None, longitud=None, num_vueltas=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.longitud = longitud
        self.num_vueltas = num_vueltas

    def __str__(self):
        tostring = "Datos del circuito: \nNombre del circuito: " + self.nombre
        if self.ubicacion is None:
            tostring += "\nUbicacion: " + self.ubicacion
        if self.longitud is None:
            tostring += "\nLongitud: " + str(self.longitud) + "km"
        if self.num_vueltas is None:
            tostring += "\nNumero de Vueltas: " + str(self.num_vueltas)
        return tostring + "\n"