__author__ = 'pablolmedorado'

from unittest import TestCase
from src.Circuito import Circuito


class TestCircuito(TestCase):
    def test_str(self):
        """
        Prueba del metodo ToString

        Dados unos datos, comprueba que se crea correctamente el objeto Circuito y que muestra bien los datos

        :return: Resultado de la prueba
        :rtype: Boolean
        """
        circ = Circuito("CircuitoDePrueba", "UbDePrueba", 12345, 99)
        string = "Datos del circuito: \nNombre del circuito: " + "CircuitoDePrueba"
        string += "\nUbicacion: " + "UbDePrueba"
        string += "\nLongitud: " + "12345" + "km"
        string += "\nNumero de Vueltas: " + "99" + "\n"
        self.assertEqual(string, str(circ))