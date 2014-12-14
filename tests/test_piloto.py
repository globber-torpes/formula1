from unittest import TestCase
from src.Piloto import *

__author__ = 'manolo'


class TestPiloto(TestCase):
    def test_str(self):
        """
        Prueba del metodo ToString
        Dados unos datos, comprueba que se crea correctamente el objeto Piloto y que muestra bien los datos

        :return: Resultado de la prueba
        :rtype: Boolean
        """
        pil = Piloto("PRUEBA", "pilotoprueba", "apellidoprueba", "renault", "ferrari", "espana", "21-04-88")
        string = "Datos del piloto: \nIdentificador del piloto: " + "PRUEBA"
        string += "\nNombre completo: " + "pilotoprueba"
        string += " " + "apellidoprueba"
        string += "\nEquipo: " + "renault"
        string += "\nEquipo Anterior: " + "ferrari"
        string += "\nNacionalidad: " + "espana"
        string += "\nFecha de Nacimiento: " + "21-04-88" + "\n"
        self.assertEqual(string, str(pil))