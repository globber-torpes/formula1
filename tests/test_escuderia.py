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
        when(escuderia1).agregar_piloto(piloto1.id_piloto(1))
        piloto2 = mock(Piloto)

        piloto2.id_piloto(2)
        print piloto2.id_piloto()
        print piloto1.id_piloto()
        print escuderia1.eliminar_piloto(piloto2.id_piloto(2))
        self.assertTrue(escuderia1.eliminar_piloto(piloto2.id_piloto(1)), escuderia1.eliminar_piloto(piloto1.id_piloto(2)))


    def test_sustituir_piloto(self):
         escuderia1 = mock(Escuderia)
         piloto1 = mock(Piloto)
         piloto2 = mock(Piloto)

         premio = mock(GranPremio)

         escuderia1.sustituir_piloto(piloto1, piloto2)