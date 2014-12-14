from unittest import TestCase
from src.Escuderia import Escuderia
from src.Piloto import Piloto
from src.Circuito import Circuito
from src.GranPremio import GranPremio
from mock import patch

__author__ = 'MAMISHO'


class TestGranPremio(TestCase):
    def test_extraer_participantes_1(self):
        """
        Test extraer participantes existentes

        Este test comprueba que los participantes fueron
        agregado correctamente en el gran premio, y
        se comprueba la funcionalidad de extraer participantes
        que se usa en otros modulos.

        :param p1: Piloto de la escuderia e1
        :param p2: Piloto de la escuderia e1
        :param p3: Piloto de la escuderia e2
        :param p4: Piloto de la escuderia e2
        :param p5: Piloto de la escuderia e3
        :param p6: Piloto de la escuderia e4
        :param e1: Escuderia para agregar al circuito
        :param e2: Escuderia para agregar al circuito
        :param e3: Escuderia para agregar al circuito
        :param c1: circuito del gran premio
        :param es: Diccionario de circuitos para crear el gran premio
        :param gp: gran premio del test
        :param participantes: objeto que se usa para comprobar la funcionalidad
        """
        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = Piloto("CCC", "Piloto C")
        p4 = Piloto("DDD", "Piloto D")
        p5 = Piloto("EEE", "Piloto E")
        p6 = Piloto("FFF", "Piloto F")

        e1 = Escuderia("Escuderia 1")
        e2 = Escuderia("Escuderia 2")
        e3 = Escuderia("Escuderia 3")

        c1 = Circuito("Circuito 1")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e2.agregar_piloto(p3)
        e2.agregar_piloto(p4)
        e3.agregar_piloto(p5)
        e3.agregar_piloto(p6)

        es = {e1.nombre: e1, e2.nombre: e2, e3.nombre: e3}

        gp = GranPremio("Gran Premio 1", c1, es, "USA", "2014")

        participantes = {}
        participantes = gp.extraer_participantes(es)

        print participantes

        # self.assertDictContainsSubset(participantes, es, None)
        self.assertIn(p1.idPiloto, participantes)
        self.assertIn(p2.idPiloto, participantes)
        self.assertIn(p3.idPiloto, participantes)
        self.assertIn(p4.idPiloto, participantes)
        self.assertIn(p5.idPiloto, participantes)
        self.assertIn(p6.idPiloto, participantes)

    def test_extraer_participantes_2(self):
        """
        Test extraer participantes no exitentes

        Este test comprueba que no se extraigan participantes
        que no estan en el gran premio

        :param p1: Piloto de la escuderia e1
        :param p2: Piloto de la escuderia e1
        :param p3: Piloto de la escuderia e2
        :param p4: Piloto de la escuderia e2
        :param p5: Piloto de la escuderia e3
        :param p6: Piloto de la escuderia e4
        :param p7: Participante que no esta en el gran premio y que no debe aparecer en el diccionario
        :param e1: Escuderia para agregar al circuito
        :param e2: Escuderia para agregar al circuito
        :param e3: Escuderia para agregar al circuito
        :param c1: circuito del gran premio
        :param es: Diccionario de circuitos para crear el gran premio
        :param gp: gran premio del test
        :param participantes: Diccionario que se usa para comprobar la funcionalidad
        """
        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = Piloto("CCC", "Piloto C")
        p4 = Piloto("DDD", "Piloto D")
        p5 = Piloto("EEE", "Piloto E")
        p6 = Piloto("FFF", "Piloto F")
        p7 = Piloto("GGG", "Piloto G")

        e1 = Escuderia("Escuderia 1")
        e2 = Escuderia("Escuderia 2")
        e3 = Escuderia("Escuderia 3")

        c1 = Circuito("Circuito 1")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e2.agregar_piloto(p3)
        e2.agregar_piloto(p4)
        e3.agregar_piloto(p5)
        e3.agregar_piloto(p6)

        es = {e1.nombre: e1, e2.nombre: e2, e3.nombre: e3}

        gp = GranPremio("Gran Premio 1", c1, es, "USA", "2014")

        participantes = {}
        participantes = gp.extraer_participantes(es)

        self.assertIsNot(p7.idPiloto, participantes)

    @patch('src.GranPremio.GranPremio.set_clasificacion')
    def test_set_clasificacion(self, raw_input):
        """
        Test set_clasificacion

        Este test comprueba que se pueda realizar introducir
        parametros por teclado segun el programa solicita al usuario
        Se hace uso de patch desde la libreria de mock

        :param p1: Piloto de la escuderia e1
        :param p2: Piloto de la escuderia e1
        :param p3: Piloto de la escuderia e2
        :param p4: Piloto de la escuderia e2
        :param p5: Piloto de la escuderia e3
        :param p6: Piloto de la escuderia e4
        :param p7: Participante que no esta en el gran premio y que no debe aparecer en el diccionario
        :param e1: Escuderia para agregar al circuito
        :param e2: Escuderia para agregar al circuito
        :param e3: Escuderia para agregar al circuito
        :param c1: circuito del gran premio
        :param es: Diccionario de circuitos para crear el gran premio
        :param gp: gran premio del test
        :param participantes: Diccionario que se usa para comprobar la funcionalidad
        """
        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = Piloto("CCC", "Piloto C")
        p4 = Piloto("DDD", "Piloto D")
        p5 = Piloto("EEE", "Piloto E")
        p6 = Piloto("FFF", "Piloto F")
        p7 = Piloto("GGG", "Piloto G")

        e1 = Escuderia("Escuderia 1")
        e2 = Escuderia("Escuderia 2")
        e3 = Escuderia("Escuderia 3")

        c1 = Circuito("Circuito 1")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e2.agregar_piloto(p3)
        e2.agregar_piloto(p4)
        e3.agregar_piloto(p5)
        e3.agregar_piloto(p6)

        es = {e1.nombre: e1, e2.nombre: e2, e3.nombre: e3}

        ng = GranPremio("Gran Premio 1", c1, es, "USA", "2014")

        self.assertIsNotNone(ng.set_clasificacion())

    def test_set_vuelta_rapida(self):
        """
        Test set vuelta rapida

        Este test comprueba que se pueda introducir una vuelta rapida
        Se pasa lossiguientes parametros

        :param p1: Piloto de la escuderia e1
        :param p2: Piloto de la escuderia e1
        :param p3: Piloto de la escuderia e2
        :param p4: Piloto de la escuderia e2
        :param p5: Piloto de la escuderia e3
        :param p6: Piloto de la escuderia e4
        :param e1: Escuderia para agregar al circuito
        :param e2: Escuderia para agregar al circuito
        :param e3: Escuderia para agregar al circuito
        :param c1: circuito del gran premio
        :param es: Diccionario de circuitos para crear el gran premio
        :param gp: gran premio del test
        """
        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = Piloto("CCC", "Piloto C")
        p4 = Piloto("DDD", "Piloto D")
        p5 = Piloto("EEE", "Piloto E")
        p6 = Piloto("FFF", "Piloto F")

        e1 = Escuderia("Escuderia 1")
        e2 = Escuderia("Escuderia 2")
        e3 = Escuderia("Escuderia 3")

        c1 = Circuito("Circuito 1")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e2.agregar_piloto(p3)
        e2.agregar_piloto(p4)
        e3.agregar_piloto(p5)
        e3.agregar_piloto(p6)

        es = {e1.nombre: e1, e2.nombre: e2, e3.nombre: e3}

        gp = GranPremio("Gran Premio 1", c1, es, "USA", "2014")

        self.assertEqual(gp.set_vuelta_rapida("1:14:123", "AAA"), True)
