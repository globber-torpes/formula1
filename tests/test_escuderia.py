from unittest import TestCase

from mockito import *

from src.Escuderia import *

from src.Piloto import *

from src.GranPremio import *


__author__ = 'francisco'


class TestEscuderia(TestCase):
    def test_agregar_piloto(self):

        piloto1 = mock(Piloto)
        escuderia1 = mock(Escuderia)

        piloto2 = mock(Piloto)

        print escuderia1.agregar_piloto("hola")



    def test_sustituir_piloto(self):
         escuderia1 = mock(Escuderia)
         piloto1 = mock(Piloto)
         piloto2 = mock(Piloto)

         premio = mock(GranPremio)

         escuderia1.sustituir_piloto(piloto1, piloto2)