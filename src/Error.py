class TipoException(Exception):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return repr("El parametro " + self.param + " no es del tipo esperado.")

class ActivosException(Exception):
    def __init__(self, escuderia):
        self.escuderia = escuderia

    def __str__(self):
        return repr("La escuderia " + self.escuderia + " no posee 2 pilotos activos")

class FormatoException(Exception):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return repr("El parametro " + self.param + " no cumple el formato requerido.")