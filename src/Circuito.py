class Circuito(object):
    """Representa un circuito de Formula 1"""

    def __init__(self, nombre, ubicacion=None, longitud=None, num_vueltas=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.longitud = longitud
        self.num_vueltas = num_vueltas

    def __str__(self):
        """
        Metodo ToString

        Muestra una representacion en texto de la instancia sobre la que se ejecuta.

        :return: Cadena con los datos del circuito correspondiente
        :rtype: String
        """
        tostring = "Datos del circuito: \nNombre del circuito: " + self.nombre
        if self.ubicacion is not None:
            tostring += "\nUbicacion: " + self.ubicacion
        if self.longitud is not None:
            tostring += "\nLongitud: " + str(self.longitud) + "km"
        if self.num_vueltas is not None:
            tostring += "\nNumero de Vueltas: " + str(self.num_vueltas)
        return tostring + "\n"